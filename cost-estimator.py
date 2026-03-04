from dataclasses import dataclass
from typing import List

@dataclass
class Material:
    name: str
    cost_per_kg: float      # ₹ per kg
    weight_g: float         # grams used

@dataclass
class PrintJob:
    materials: List[Material]
    print_time_hr: float
    electricity_rate_per_kwh: float
    printer_power_w: float
    machine_rate_per_hr: float
    labour_rate_per_hr: float
    labour_time_hr: float
    failure_margin_percent: float
    profit_margin_percent: float


def calculate_print_cost(job: PrintJob):
    bom = []
    total_material_cost = 0

    # ---- Material Cost ----
    for mat in job.materials:
        cost = (mat.cost_per_kg / 1000) * mat.weight_g
        total_material_cost += cost
        bom.append((f"Material: {mat.name}", cost))

    # ---- Machine Cost ----
    machine_cost = job.print_time_hr * job.machine_rate_per_hr
    bom.append(("Machine usage", machine_cost))

    # ---- Electricity Cost ----
    energy_kwh = (job.printer_power_w / 1000) * job.print_time_hr
    electricity_cost = energy_kwh * job.electricity_rate_per_kwh
    bom.append(("Electricity", electricity_cost))

    # ---- Labour Cost ----
    labour_cost = job.labour_time_hr * job.labour_rate_per_hr
    bom.append(("Labour", labour_cost))

    # ---- Base Cost ----
    base_cost = (
        total_material_cost
        + machine_cost
        + electricity_cost
        + labour_cost
    )

    # ---- Failure Margin ----
    failure_cost = base_cost * (job.failure_margin_percent / 100)
    bom.append(("Failure allowance", failure_cost))

    # ---- Profit ----
    profit = (base_cost + failure_cost) * (job.profit_margin_percent / 100)
    bom.append(("Profit", profit))

    total_price = base_cost + failure_cost + profit

    return bom, total_price


def print_bom(bom, total_price):
    print("\n===== FDM PRINT BILL OF MATERIAL =====")
    for item, cost in bom:
        print(f"{item:<30} ₹ {cost:8.2f}")
    print("-------------------------------------")
    print(f"{'TOTAL PRICE':<30} ₹ {total_price:8.2f}")
    print("=====================================\n")


# -------- Example Usage --------
if __name__ == "__main__":
    materials = [
        Material("PLA", cost_per_kg=1200, weight_g=85),
        Material("PVA Support", cost_per_kg=3500, weight_g=12),
    ]

    job = PrintJob(
        materials=materials,
        print_time_hr=6.5,
        electricity_rate_per_kwh=8.0,
        printer_power_w=250,
        machine_rate_per_hr=50,
        labour_rate_per_hr=200,
        labour_time_hr=0.5,
        failure_margin_percent=10,
        profit_margin_percent=20,
    )

    bom, total = calculate_print_cost(job)
    print_bom(bom, total)
