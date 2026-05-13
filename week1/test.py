from pathlib import Path
import argparse
import shutil
import sys
import pycolmap


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}


def find_images(image_dir: Path) -> list[Path]:
    return sorted(
        p for p in image_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS
    )


def run_pycolmap_sparse(
    image_dir: Path,
    output_dir: Path,
    camera_model: str,
    num_threads: int,
    max_image_size: int,
    force: bool,
):
    image_dir = image_dir.resolve()
    output_dir = output_dir.resolve()

    if not image_dir.exists() or not image_dir.is_dir():
        raise FileNotFoundError(f"Image directory does not exist or is not a directory: {image_dir}")

    images = find_images(image_dir)
    if not images:
        raise ValueError(
            f"No images found in {image_dir}. Expected one of: {', '.join(sorted(IMAGE_EXTENSIONS))}"
        )

    database_path = output_dir / "database.db"
    sparse_dir = output_dir / "sparse"

    output_dir.mkdir(parents=True, exist_ok=True)

    if (database_path.exists() or sparse_dir.exists()) and not force:
        raise FileExistsError(
            "Output already contains previous results. Re-run with --force to overwrite."
        )

    if database_path.exists() and force:
        database_path.unlink()
    if sparse_dir.exists() and force:
        shutil.rmtree(sparse_dir)
    sparse_dir.mkdir(parents=True, exist_ok=True)

    print("PyCOLMAP sparse reconstruction")
    print(f"  image directory : {image_dir}")
    print(f"  number of images: {len(images)}")
    print(f"  output directory: {output_dir}")
    print(f"  camera model    : {camera_model}")
    print(f"  threads         : {num_threads}")
    print(f"  max image size  : {max_image_size}")
    print(f"  overwrite       : {force}")

    # Reader options control camera assumptions for feature extraction.
    reader_options = pycolmap.ImageReaderOptions()
    reader_options.camera_model = camera_model

    # Feature extraction options 
    extraction_options = pycolmap.FeatureExtractionOptions()
    extraction_options.num_threads = num_threads
    extraction_options.max_image_size = max_image_size

    print("Extracting features...")
    pycolmap.extract_features(
        database_path,
        image_dir,
        reader_options=reader_options,
        extraction_options=extraction_options,
    )

    print("Matching features exhaustively...")
    pycolmap.match_exhaustive(database_path)

    print("Running incremental mapping...")
    reconstructions = pycolmap.incremental_mapping(
        database_path,
        image_dir,
        sparse_dir,
    )

    if len(reconstructions) == 0:
        print("No reconstruction was produced.")
        return

    for idx, reconstruction in reconstructions.items():
        print(f"\nReconstruction #{idx}")
        print(reconstruction.summary())
        reconstruction.write(sparse_dir / str(idx))

    print(f"\nWrote reconstructions to: {sparse_dir}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Run a minimal sparse SfM pipeline with pycolmap: feature extraction, "
            "exhaustive matching, and incremental mapping."
        )
    )
    parser.add_argument(
        "--image-dir",
        required=True,
        help="Path to a folder containing input images.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Path to a folder where database.db and sparse/ will be written.",
    )
    parser.add_argument(
        "--camera-model",
        default="SIMPLE_RADIAL",
        help="COLMAP camera model to use during image reading (default: SIMPLE_RADIAL).",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=2,
        help="Number of CPU threads for feature extraction (default: 2).",
    )
    parser.add_argument(
        "--max-image-size",
        type=int,
        default=1600,
        help="Maximum image size (in pixels) for feature extraction. Larger images will be downscaled (default: 1600).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing database/sparse outputs in --output-dir.",
    )
    args = parser.parse_args()

    if args.threads < 1:
        parser.error("--threads must be >= 1")
    if args.max_image_size < 1:
        parser.error("--max-image-size must be >= 1")

    try:
        run_pycolmap_sparse(
            Path(args.image_dir),
            Path(args.output_dir),
            camera_model=args.camera_model,
            num_threads=args.threads,
            max_image_size=args.max_image_size,
            force=args.force,
        )
    except (FileNotFoundError, FileExistsError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Unexpected pycolmap error: {exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
