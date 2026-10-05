"""
Problem: Plotting Academic Benchmarks with Matplotlib
Author: Bhavishya Dewangan
"""
try:
    import matplotlib.pyplot as plt

    def generate_chart():
        semesters = ["Sem 1", "Sem 2", "Sem 3 (Current)"]
        sgpa = [8.40, 8.65, 8.85]

        plt.figure(figsize=(7, 4))
        plt.plot(semesters, sgpa, marker='o', color='#10B981', linewidth=2.5, markersize=8)
        plt.title("Academic Performance Trajectory", fontsize=14, fontweight='bold')
        plt.xlabel("Academic Term", fontsize=11)
        plt.ylabel("SGPA", fontsize=11)
        plt.ylim(7.5, 10.0)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.savefig("academic_trajectory.png")
        print("Chart saved as academic_trajectory.png")

    if __name__ == "__main__":
        generate_chart()
except ImportError:
    print("Matplotlib not installed. Install via: pip install matplotlib")
