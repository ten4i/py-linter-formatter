def format_linter_error(error: dict) -> dict:
    return {
        new: error[old]
        for old, new in {
            "line_number": "line",
            "column_number": "column",
            "text": "message",
            "code": "name", }.items()} | {"source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            {
                "line": err["line_number"],
                "column": err["column_number"],
                "message": err["text"],
                "name": err["code"],
                "source":"flake8",
            }
            for err in errors
        ],
        "path": file_path,
        "status": "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [
                {
                    "line": err["line_number"],
                    "column": err["column_number"],
                    "message": err["text"],
                    "name": err["code"],
                    "source": "flake8",
                }
                for err in errors
            ],
            "path": filename,
            "status": "failed" if errors else "passed",
        }
        for filename, errors in linter_report.items()
    ]
