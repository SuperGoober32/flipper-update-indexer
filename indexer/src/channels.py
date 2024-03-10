from .models import Channel


development_channel = Channel(
    id="development",
    title="Development Channel",
    description="Latest builds, might sometimes be unstable",
)
# release_candidate_channel = Channel(
#     id="release-candidate",
#     title="Release Candidate Channel",
#     description="This is going to be released soon, undergoing QA tests now",
# )
release_channel = Channel(
    id="release",
    title="Stable Release Channel",
    description="Less frequent, more stable releases",
)
