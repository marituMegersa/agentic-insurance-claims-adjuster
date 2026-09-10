from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.insurance_claims_adjuster.schemas import AgenticInsuranceClaimsAdjusterSessionCreate, AgenticInsuranceClaimsAdjusterSessionResponse
from app.domain.insurance_claims_adjuster.service import AgenticInsuranceClaimsAdjusterService

router = APIRouter(prefix="/api/v1/insurance_claims_adjuster", tags=["Agentic Insurance Claims Adjuster Domain"])

@router.post("/sessions", response_model=AgenticInsuranceClaimsAdjusterSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticInsuranceClaimsAdjusterSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Insurance Claims Adjuster.
    """
    return AgenticInsuranceClaimsAdjusterService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticInsuranceClaimsAdjusterSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticInsuranceClaimsAdjusterService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
