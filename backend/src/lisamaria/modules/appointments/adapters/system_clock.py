"""PT: Adapter de relógio real. EN: Real clock adapter."""

from datetime import UTC, datetime


class SystemClock:
    """PT: Lê o relógio do sistema em UTC. EN: Read the system clock in UTC."""

    def now(self) -> datetime:
        """PT: Instante atual. EN: Current instant."""
        return datetime.now(UTC)
