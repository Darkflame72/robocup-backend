# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.team import Team
from app.models.user import User
