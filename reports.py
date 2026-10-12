"""Student performance reports."""
from collections import Counter
import validators as v

PASS_MARK = 40


def performance_report(students):
    print("\n========== PERFORMANCE REPORT ==========")
    if not students:
        print("  No records available.")
        return
    records = list(students.values())
    ranked = sorted(records, key=lambda s: s["average"], reverse=True)

    print("\n  Rank list:")
    for rank, s in enumerate(ranked, 1):
        print(f"   {rank}. {s['name']} ({s['roll']}) - {s['average']}% [{s['grade']}]")

    class_avg = round(sum(s["average"] for s in records) / len(records), 2)
    passed = [s for s in records if all(m >= PASS_MARK for m in s["marks"].values())]
    print(f"\n  Total students : {len(records)}")
    print(f"  Class average  : {class_avg}%")
    print(f"  Topper         : {ranked[0]['name']} ({ranked[0]['average']}%)")
    print(f"  Lowest scorer  : {ranked[-1]['name']} ({ranked[-1]['average']}%)")
    print(f"  Pass percentage: {round(len(passed) / len(records) * 100, 2)}%")

    print("\n  Grade distribution:")
    counts = Counter(s["grade"] for s in records)
    for grade in ["A+", "A", "B", "C", "D", "F"]:
        print(f"   {grade:<3}: {'#' * counts.get(grade, 0)} ({counts.get(grade, 0)})")

    print("\n  Subject-wise averages / highest:")
    for subject in v.SUBJECTS:
        scores = [s["marks"][subject] for s in records]
        print(f"   {subject:<10}: avg {round(sum(scores)/len(scores), 2):>6} | highest {max(scores)}")
