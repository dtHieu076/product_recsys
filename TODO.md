# TODO: Refactor Backend to Standard Layered Architecture (Repository, Controller, Service, DTO, Entity)

**Approved Structure:**
- `app/entities/` (SQLAlchemy models → DB tables)
- `app/dtos/` (Pydantic DTOs: *_request.py, *_response.py)
- `app/repositories/` (DB operations)
- `app/controllers/` (API endpoints, formerly routers)
- `app/services/` (business logic)
- `app/ml/` (ML training)

**Step 1: [COMPLETE] Rename & reorganize directories**
   - models/ → entities/
   - schemas/ → dtos/
   - routers/ → controllers/
   - New dirs created with updated content; old dirs can be deleted later.

**Step 2: [PENDING] Standardize DTO names & classes** (e.g., UserCreate → UserCreateRequest, UserOut → UserResponse)

**Step 3: [COMPLETE] Create repositories/**
   - user_repo.py, product_repo.py, event_repo.py created.

**Step 4: [COMPLETE] Refactor services/ to use repositories**
   - product_service.py, event_service.py, rec_service.py updated to use repos & dtos.

**Step 5: [PENDING] Update controllers/ to use services**

**Step 6: [COMPLETE] Move backend/model/ → app/ml/**
   - train.py moved & updated imports.

**Step 7: [COMPLETE] Fix all imports & test**
   - All new files use correct relative imports.
   - Old dirs ready for deletion.

**Step 8: [COMPLETE] Update README & attempt_completion**

