from .efficient_sam import build_efficient_sam

def build_efficient_sam_vitt():
    return build_efficient_sam(
        encoder_patch_embed_dim=192,
        encoder_num_heads=3,
        checkpoint="models/efficient_sam_vitt.pt",
    ).eval()


def build_efficient_sam_vits():
    return build_efficient_sam(
        encoder_patch_embed_dim=384,
        encoder_num_heads=6,
        checkpoint="models/efficient_sam_vits.pt",
    ).eval()
