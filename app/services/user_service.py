from PureCloudPlatformClientV2.models import AnalyticsUserDetail
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.genesys.genesys_api_client import GenesysApiClient
from app.genesys.models import PrimaryPresence


def insert_primary_presence(db: Session, interval: str) -> None:
    try:
        analytics_users_details = GenesysApiClient().get_analytics_users_details(
            interval
        )
        primary_presences = _extract_primary_presences(analytics_users_details)
        _bulk_insert_primary_presences(db, primary_presences)
    except Exception as e:
        db.rollback()
        raise RuntimeError(
            f"Erro ao inserir dados na tabela primary presence: {str(e)}"
        )


def _extract_primary_presences(
    analytics_users_details: list[AnalyticsUserDetail],
) -> list[PrimaryPresence]:
    primary_presences_list = []

    for user_detail in analytics_users_details:
        if not user_detail.primary_presence:
            continue

        for primary_presence in user_detail.primary_presence:
            primary_presences_list.append(
                PrimaryPresence(
                    primary_presence_id=primary_presence.organization_presence_id,
                    user_id=user_detail.user_id,
                    start_time=primary_presence.start_time,
                    end_time=primary_presence.end_time,
                    system_presence=primary_presence.system_presence,
                    organization_presence_id=primary_presence.organization_presence_id,
                )
            )

    return primary_presences_list


def _bulk_insert_primary_presences(
    db: Session, primary_presences: list[PrimaryPresence]
) -> None:
    try:
        db.bulk_save_objects(primary_presences, update_changed_only=True)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise SQLAlchemyError(
            f"Erro no banco de dados durante a inserção em massa: {str(e)}"
        )
