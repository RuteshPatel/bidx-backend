from app.core.database import SessionLocal
from app.models.role import Role


def seed_roles():
    db = SessionLocal()

    default_roles = [
        {"name": "super_admin", "description": "System Super Admin"},
        {"name": "admin", "description": "Tenant Admin"},
        {"name": "owner", "description": "Team Owner"},
        {"name": "player", "description": "Player"}
    ]

    for role in default_roles:
        existing = db.query(Role).filter(Role.name == role["name"]).first()

        if not existing:
            new_role = Role(
                name=role["name"],
                description=role["description"]
            )
            db.add(new_role)
            print(f"Added role: {role['name']}")

    db.commit()
    print("Roles seeded successfully")


if __name__ == "__main__":
    seed_roles()
