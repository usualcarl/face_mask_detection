import os
from collections import defaultdict
from PIL import Image

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CLASSES = ['with_mask', 'without_mask']


def count_images_by_class(data_dir):
    counts = {}
    for cls in CLASSES:
        cls_dir = os.path.join(data_dir, cls)
        if not os.path.isdir(cls_dir):
            counts[cls] = 0
            continue
        counts[cls] = sum(
            1 for name in os.listdir(cls_dir)
            if name.lower().endswith(('.jpg', '.jpeg', '.png'))
        )
    return counts


def read_sample_images(data_dir, n_per_class=2):
    samples = defaultdict(list)
    for cls in CLASSES:
        cls_dir = os.path.join(data_dir, cls)
        if not os.path.isdir(cls_dir):
            continue
        files = [
            name for name in os.listdir(cls_dir)
            if name.lower().endswith(('.jpg', '.jpeg', '.png'))
        ]
        files = sorted(files)[:n_per_class]
        for f in files:
            path = os.path.join(cls_dir, f)
            try:
                img = Image.open(path)
                img.verify()  # Быстрая проверка целостности
                samples[cls].append((f, img.size))
            except Exception as e:
                samples[cls].append((f, f'ERROR: {e}'))
    return samples


def main():
    print(f"[INFO] Data dir: {os.path.abspath(DATA_DIR)}")
    counts = count_images_by_class(DATA_DIR)
    print("[INFO] Image counts:")
    for cls, c in counts.items():
        print(f"  - {cls}: {c}")

    samples = read_sample_images(DATA_DIR, n_per_class=3)
    print("[INFO] Sample images (filename, size):")
    for cls, items in samples.items():
        for fname, meta in items:
            print(f"  - {cls}: {fname} => {meta}")

    # Простая проверка баланса классов
    if all(k in counts for k in CLASSES):
        total = sum(counts.values())
        if total > 0:
            pct = {k: round(v / total * 100, 2) for k, v in counts.items()}
            print("[INFO] Class distribution (%):", pct)


if __name__ == '__main__':
    main()
