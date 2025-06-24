import tkinter as tk
from metrics import Metrics
from dynamic_agent import DynamicAgent
from static_agent import StaticAgent


def format_summary(summary: dict) -> str:
    """Format the metrics summary for display."""
    lines = [f"{k}: {v}" for k, v in summary.items()]
    return "\n".join(lines)


def run():
    """Launch the side-by-side agent comparison UI."""
    root = tk.Tk()
    root.title("Agent Comparison")

    tk.Label(root, text="Conversation script (one step per line):").pack(anchor="w")
    script_text = tk.Text(root, width=60, height=10)
    script_text.pack()

    result_frame = tk.Frame(root)
    result_frame.pack(fill="both", expand=True, pady=10)

    tk.Label(result_frame, text="StaticAgent Metrics:").grid(row=0, column=0, sticky="w")
    tk.Label(result_frame, text="DynamicAgent Metrics:").grid(row=0, column=1, sticky="w")

    static_var = tk.StringVar()
    dynamic_var = tk.StringVar()

    tk.Label(result_frame, textvariable=static_var, justify="left").grid(row=1, column=0, padx=10, sticky="nw")
    tk.Label(result_frame, textvariable=dynamic_var, justify="left").grid(row=1, column=1, padx=10, sticky="nw")

    def on_run():
        raw = script_text.get("1.0", tk.END)
        lines = [line.strip() for line in raw.strip().splitlines() if line.strip()]
        metrics_static = Metrics()
        metrics_dynamic = Metrics()

        dyn_agent = DynamicAgent(metrics_dynamic)
        static_agent = StaticAgent(metrics_static, turns=len(lines))

        dyn_summary = dyn_agent.converse(lines)
        static_summary = static_agent.converse()

        dynamic_var.set(format_summary(dyn_summary))
        static_var.set(format_summary(static_summary))

    tk.Button(root, text="Run", command=on_run).pack(pady=5)
    root.mainloop()


if __name__ == "__main__":
    run()
