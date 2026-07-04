import tkinter as tk
from tkinter import ttk, simpledialog, filedialog

from styles import *
from network_tools import *
from report import save_report, write_log


def start_app():

    root = tk.Tk()
    root.title("Network Troubleshooting Simulator")
    root.geometry("900x720")
    root.configure(bg=BACKGROUND)

    # ==========================
    # Title
    # ==========================

    title = tk.Label(
        root,
        text="🌐 NETWORK TROUBLESHOOTING SIMULATOR",
        font=TITLE_FONT,
        bg=BACKGROUND,
        fg=TITLE_COLOR
    )

    title.pack(pady=15)

    # ==========================
    # Status Label
    # ==========================

    status_label = tk.Label(
        root,
        text="🟡 Status : Ready",
        font=("Arial",13,"bold"),
        bg=BACKGROUND,
        fg=STATUS_READY
    )

    status_label.pack()

    # ==========================
    # Progress Bar
    # ==========================

    progress = ttk.Progressbar(
        root,
        orient="horizontal",
        length=450,
        mode="determinate"
    )

    progress.pack(pady=10)

    # ==========================
    # Buttons Frame
    # ==========================

    button_frame = tk.Frame(
        root,
        bg=BACKGROUND
    )

    button_frame.pack(pady=10)

    # ==========================
    # Output Title
    # ==========================

    output_title = tk.Label(
        root,
        text="Network Output",
        font=("Arial",13,"bold"),
        bg=BACKGROUND,
        fg=TITLE_COLOR
    )

    output_title.pack()

    # ==========================
    # Output Box
    # ==========================

    output = tk.Text(
        root,
        width=95,
        height=18,
        font=OUTPUT_FONT
    )

    output.pack(pady=10)

    # ==========================
    # Footer
    # ==========================

    footer = tk.Label(
        root,
        text="Ready",
        relief=tk.SUNKEN,
        anchor="w"
    )

    footer.pack(
        side=tk.BOTTOM,
        fill=tk.X
    )
        # ======================================================
    # FUNCTIONS
    # ======================================================

    def reset_progress():
        progress["value"] = 0

    def finish_progress():
        progress["value"] = 100
        root.update()
        root.after(1000, reset_progress)

    # ------------------------------------------------------
    # Internet Connectivity Check
    # ------------------------------------------------------

    def check_network():

        output.delete(1.0, tk.END)

        footer.config(text="Checking Internet Connection...")

        progress["value"] = 25
        root.update()

        if check_internet():

            status_label.config(
                text="🟢 Status : Connected",
                fg=STATUS_CONNECTED
            )

            output.insert(
                tk.END,
                "Internet Status : CONNECTED\n\n"
            )

            output.insert(
                tk.END,
                "✓ Internet connection is working properly.\n"
            )

            write_log("Internet Check")

            footer.config(
                text="Internet Check Completed"
            )

        else:

            status_label.config(
                text="🔴 Status : Disconnected",
                fg=STATUS_DISCONNECTED
            )

            output.insert(
                tk.END,
                "Internet Status : NOT CONNECTED\n\n"
            )

            output.insert(
                tk.END,
                "Possible Causes:\n"
            )

            output.insert(
                tk.END,
                "• Wi-Fi disconnected\n"
                "• Router powered OFF\n"
                "• ISP issue\n\n"
            )

            output.insert(
                tk.END,
                "Suggested Solutions:\n"
                "1. Restart Router\n"
                "2. Reconnect Wi-Fi\n"
                "3. Contact ISP\n"
            )

            write_log("Internet Check Failed")

            footer.config(
                text="Internet Not Available"
            )

        finish_progress()

    # ------------------------------------------------------
    # Ping Test
    # ------------------------------------------------------

    def run_ping():

        host = simpledialog.askstring(
            "Ping Test",
            "Enter Website or IP:"
        )

        if not host:
            return

        output.delete(1.0, tk.END)

        footer.config(text="Running Ping Test...")

        progress["value"] = 30
        root.update()

        result = ping(host)

        output.insert(
            tk.END,
            result
        )

        write_log(f"Ping Test : {host}")

        footer.config(
            text="Ping Test Completed"
        )

        finish_progress()

    # ------------------------------------------------------
    # DNS Lookup
    # ------------------------------------------------------

    def run_dns():

        website = simpledialog.askstring(
            "DNS Lookup",
            "Enter Website:"
        )

        if not website:
            return

        output.delete(1.0, tk.END)

        footer.config(text="Running DNS Lookup...")

        progress["value"] = 30
        root.update()

        ip = dns_lookup(website)

        if ip:

            output.insert(
                tk.END,
                f"Website : {website}\n\n"
            )

            output.insert(
                tk.END,
                f"IP Address : {ip}"
            )

        else:

            output.insert(
                tk.END,
                "DNS Resolution Failed"
            )

        write_log(f"DNS Lookup : {website}")

        footer.config(
            text="DNS Lookup Completed"
        )

        finish_progress()

    # ------------------------------------------------------
    # IP Configuration
    # ------------------------------------------------------

    def show_ip():

        output.delete(1.0, tk.END)

        footer.config(
            text="Loading IP Configuration..."
        )

        progress["value"] = 30
        root.update()

        output.insert(
            tk.END,
            ip_config()
        )

        write_log("Viewed IP Configuration")

        footer.config(
            text="IP Configuration Loaded"
        )

        finish_progress()
            # ======================================================
    # BUTTONS
    # ======================================================

    internet_btn = tk.Button(
        button_frame,
        text="Check Internet",
        font=("Arial", 11, "bold"),
        width=18,
        command=check_network,
        bg="#4CAF50",
        fg="white"
    )

    internet_btn.grid(row=0, column=0, padx=8, pady=5)

    ping_btn = tk.Button(
        button_frame,
        text="Ping Test",
        font=("Arial", 11, "bold"),
        width=18,
        command=run_ping,
        bg="#2196F3",
        fg="white"
    )

    ping_btn.grid(row=0, column=1, padx=8, pady=5)

    dns_btn = tk.Button(
        button_frame,
        text="DNS Lookup",
        font=("Arial", 11, "bold"),
        width=18,
        command=run_dns,
        bg="#FF9800",
        fg="white"
    )

    dns_btn.grid(row=1, column=0, padx=8, pady=5)

    ip_btn = tk.Button(
        button_frame,
        text="IP Config",
        font=("Arial", 11, "bold"),
        width=18,
        command=show_ip,
        bg="#9C27B0",
        fg="white"
    )

    ip_btn.grid(row=1, column=1, padx=8, pady=5)
        # ======================================================
    # OPTIONAL: REPORT EXPORT BUTTON
    # ======================================================

    def export_report():

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not file_path:
            return

        content = output.get(1.0, tk.END)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        footer.config(text="Report Saved Successfully")
        write_log("Report Exported")


    export_btn = tk.Button(
        root,
        text="Export Report",
        font=("Arial", 11, "bold"),
        command=export_report,
        bg="#607D8B",
        fg="white"
    )

    export_btn.pack(pady=5)
    def auto_diagnose():

     output.delete(1.0, tk.END)

    footer.config(text="Running Auto Diagnostics...")

    check_network()

    run_ping()
    run_dns()
    show_ip()

    footer.config(text="Diagnostics Completed")
    auto_btn = tk.Button(
    button_frame,
    text="Auto Diagnose",
    command=auto_diagnose,
    bg="#E91E63",
    fg="white"
)

    auto_btn.grid(row=2, column=0, columnspan=2, pady=10)
    # ======================================================
    # START APPLICATION
    # ======================================================

    root.mainloop()