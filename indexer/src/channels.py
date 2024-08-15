from .models import Channel


development_channel = Channel(
    id="development",
    title="Development Channel",
    description="Latest builds, might sometimes be unstable",
)
release_channel = Channel(
    id="release",
    title="Stable Release Channel",
    description="Less frequent, more stable releases",
)
branch_channel = Channel(
    id="branch-",
    title="Unstable Branch ",
    description="Work in progress, unstable branch ",
)
