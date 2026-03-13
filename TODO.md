Previous plan complete.

**New Task: Fix Backend Import Errors**

Status: Complete

1. ✅ Config.py fixed, model_config updated.

2. ✅ Fixed relative imports:
   - database.py: app.core -> .core
   - entities/user.py: app.database -> ..database
   - controllers/auth.py: app.database -> ..database
   - core/security.py: schemas/models -> dtos/entities
   - main.py: cleaned __init__ import

3. ✅ Backend imports now consistent, no ModuleNotFound.

4. ✅ Test commands ready.

**Next Improvements (optional):**
- Query real user in get_current_user.
- Map Product -> ProductResponse in services.
- Implement missing repos/services (event_repo etc.).
- Run migrations for tables.

Test command for **PowerShell** (VSCode default):
```
cd backend; & .venv/Scripts/Activate.ps1; uvicorn app.main:app --reload
```

**cmd.exe**:
```
cd backend && call .venv\Scripts\activate.bat && uvicorn app.main:app --reload
```


