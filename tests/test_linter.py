from datapulse.linter import MigrationLinter

def test_drop_column_is_breaking():
    linter = MigrationLinter()
    result = linter.check_breaking_change("ALTER TABLE users DROP COLUMN email;")
    assert result.is_breaking is True
