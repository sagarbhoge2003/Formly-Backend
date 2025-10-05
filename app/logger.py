import logging
import sys
from contextvars import ContextVar

# -----------------------------
# ContextVar for request_id
# -----------------------------
_request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default="-")

def get_request_id() -> str:
    return _request_id_ctx_var.get()


# -----------------------------
# Custom Logging Formatter
# -----------------------------
class RequestFormatter(logging.Formatter):
    COLORS = {
        "RESET": "\x1b[0m",
        "LEVEL_COLORS": {
            "DEBUG": "\x1b[36m",   # Cyan
            "INFO": "\x1b[32m",    # Green
            "WARNING": "\x1b[33m", # Yellow
            "ERROR": "\x1b[31m",   # Red
            "CRITICAL": "\x1b[41m" # Red background
        }
    }

    def format(self, record):
        request_id = get_request_id()
        level_color = self.COLORS["LEVEL_COLORS"].get(record.levelname, "")
        reset = self.COLORS["RESET"]

        record.request_id = request_id
        record.levelname = f"{level_color}{record.levelname}{reset}"
        record.msg = f"{record.msg}{reset}"
        return super().format(record)


def setup_logger():
    handler = logging.StreamHandler(sys.stdout)
    formatter = RequestFormatter(
        "[%(asctime)s] [%(levelname)s] [%(request_id)s] [%(message)s]",
        "%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger("uvicorn.access")
    logger.handlers = []
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


logger = setup_logger()
