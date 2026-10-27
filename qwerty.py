from importlib import import_module

try:
    plt = import_module("matplotlib.pyplot")
except ModuleNotFoundError:
    plt = None

students = {
    "Name": ["Aman", "Priya", "Ravi", "Neha", "Karan"],
    "Marks": [72, 88, 65, 94, 79],
}

print("Student Marks:")
print(f"{'Name':<10} Marks")
for name, marks in zip(students["Name"], students["Marks"]):
    print(f"{name:<10} {marks}")

print("\nAverage marks:", sum(students["Marks"]) / len(students["Marks"]))
print("Highest marks:", max(students["Marks"]))

if plt is not None:
    plt.bar(students["Name"], students["Marks"])
    plt.title("Student Marks Analysis")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()
else:
    print("Install matplotlib to display the chart: pip install matplotlib")
