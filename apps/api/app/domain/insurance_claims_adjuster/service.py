from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.insurance_claims_adjuster.models import AgenticInsuranceClaimsAdjusterSession, AgenticInsuranceClaimsAdjusterItem
from app.domain.insurance_claims_adjuster.schemas import AgenticInsuranceClaimsAdjusterSessionCreate, AgenticInsuranceClaimsAdjusterItemCreate

class AgenticInsuranceClaimsAdjusterService:
    @staticmethod
    def create_session(db: Session, data: AgenticInsuranceClaimsAdjusterSessionCreate) -> AgenticInsuranceClaimsAdjusterSession:
        db_obj = AgenticInsuranceClaimsAdjusterSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticInsuranceClaimsAdjusterSession:
        return db.query(AgenticInsuranceClaimsAdjusterSession).filter(AgenticInsuranceClaimsAdjusterSession.id == session_id).first()
