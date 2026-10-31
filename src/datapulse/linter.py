from pydantic import BaseModel

class SchemaChange(BaseModel):
    table_name: str
    change_type: str  # e.g., 'DROP_COLUMN', 'ALTER_TYPE'
    is_breaking: bool

class MigrationLinter:
    def __init__(self):
        self.rules = []

    def check_breaking_change(self, statement: str) -> SchemaChange:
        clean = statement.upper()
        if "DROP COLUMN" in clean:
            return SchemaChange(table_name="unknown", change_type="DROP_COLUMN", is_breaking=True)
        return SchemaChange(table_name="unknown", change_type="SAFE_ALTER", is_breaking=False)
