import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import plotly.express as px

def data_process(df):
    data = df.copy()
    data['order-date'] = pd.to_datetime(data['order-date'])
    return data.set_index('order-date').sort_index()


# def monthly_profit(df, from_, to_):
#     # 1. Ensure DatetimeIndex before slicing/resampling
#     data = data_process(df)
#     monthly_data = data.loc[str(from_) : str(to_)]
#     profit = monthly_data["profit"].resample("ME").sum()

#     # 2. Setup Dark Theme & Figure
#     sns.set_theme(style="dark")
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
#     fig.patch.set_facecolor("#0E1117")
#     ax.set_facecolor("#161B22")

#     # 3. Line plot with neon-cyan accents
#     sns.lineplot(
#         x=profit.index,
#         y=profit.values,
#         ax=ax,
#         color="#3B82F6",  # Bright dark-mode blue
#         linewidth=2.5,
#         marker="o",
#         markersize=6,
#         markerfacecolor="#0E1117",
#         markeredgewidth=2,
#         markeredgecolor="#3B82F6",
#     )

#     # Shaded fill under the line
#     ax.fill_between(profit.index, profit.values, color="#00F2FE", alpha=0.15)

#     # 4. Title, Labels & Colors
#     ax.set_ylabel(
#         "Profit ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
#     )

#     # 5. Currency formatting on Y-axis
#     ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

#     # 6. Dark Mode Grid & Spine Styling
#     ax.tick_params(colors="#94A3B8", labelsize=9)
#     ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
#     for spine in ax.spines.values():
#         spine.set_color("#334155")

#     return fig

# def monthly_sales(df, from_, to_):
#     # 1. Ensure DatetimeIndex before slicing/resampling
#     data = data_process(df)
#     monthly_data = data.loc[str(from_) : str(to_)]
#     sales = monthly_data["sales"].resample("ME").sum()

#     # 2. Setup Dark Theme & Figure
#     sns.set_theme(style="dark")
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
#     fig.patch.set_facecolor("#0E1117")
#     ax.set_facecolor("#161B22")

#     # 3. Line plot with vibrant purple-blue accents
#     sns.lineplot(
#         x=sales.index,
#         y=sales.values,
#         ax=ax,
#         color="#3B82F6",  # Bright dark-mode blue
#         linewidth=2.5,
#         marker="o",
#         markersize=6,
#         markerfacecolor="#0E1117",
#         markeredgewidth=2,
#         markeredgecolor="#3B82F6",
#     )

#     # Shaded fill under the line
#     ax.fill_between(sales.index, sales.values, color="#3B82F6", alpha=0.15)

#     # 4. Title, Labels & Colors
#     ax.set_ylabel(
#         "Sales ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
#     )

#     # 5. Currency formatting on Y-axis
#     ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

#     # 6. Dark Mode Grid & Spine Styling
#     ax.tick_params(colors="#94A3B8", labelsize=9)
#     ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
#     for spine in ax.spines.values():
#         spine.set_color("#334155")

#     return fig

# def quarterly_profit(df, from_, to_):
#     # 1. Ensure DatetimeIndex before slicing/resampling
#     data = data_process(df)
#     quarterly_data = data.loc[str(from_) : str(to_)]
#     profit = quarterly_data["profit"].resample("QE").sum()

#     # 2. Setup Dark Theme & Figure
#     sns.set_theme(style="dark")
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
#     fig.patch.set_facecolor("#0E1117")
#     ax.set_facecolor("#161B22")

#     # 3. Line plot with neon-cyan accents
#     sns.lineplot(
#         x=profit.index,
#         y=profit.values,
#         ax=ax,
#         color="#3B82F6",  # Bright dark-mode blue
#         linewidth=2.5,
#         marker="o",
#         markersize=6,
#         markerfacecolor="#0E1117",
#         markeredgewidth=2,
#         markeredgecolor="#3B82F6",
#     )

#     # Shaded fill under the line
#     ax.fill_between(profit.index, profit.values, color="#00F2FE", alpha=0.15)

#     # 4. Title, Labels & Colors
#     ax.set_ylabel(
#         "Profit ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
#     )

#     # 5. Currency formatting on Y-axis
#     ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

#     # 6. Dark Mode Grid & Spine Styling
#     ax.tick_params(colors="#94A3B8", labelsize=9)
#     ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
#     for spine in ax.spines.values():
#         spine.set_color("#334155")

#     return fig

# def quarterly_sales(df, from_, to_):
#     # 1. Ensure DatetimeIndex before slicing/resampling
#     data = data_process(df)
#     quarterly_data = data.loc[str(from_) : str(to_)]
#     sales = quarterly_data["sales"].resample("QE").sum()

#     # 2. Setup Dark Theme & Figure
#     sns.set_theme(style="dark")
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
#     fig.patch.set_facecolor("#0E1117")
#     ax.set_facecolor("#161B22")

#     # 3. Line plot with vibrant purple-blue accents
#     sns.lineplot(
#         x=sales.index,
#         y=sales.values,
#         ax=ax,
#         color="#3B82F6",  # Bright dark-mode blue
#         linewidth=2.5,
#         marker="o",
#         markersize=6,
#         markerfacecolor="#0E1117",
#         markeredgewidth=2,
#         markeredgecolor="#3B82F6",
#     )

#     # Shaded fill under the line
#     ax.fill_between(sales.index, sales.values, color="#3B82F6", alpha=0.15)

#     # 4. Title, Labels & Colors
#     ax.set_ylabel(
#         "Sales ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
#     )

#     # 5. Currency formatting on Y-axis
#     ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

#     # 6. Dark Mode Grid & Spine Styling
#     ax.tick_params(colors="#94A3B8", labelsize=9)
#     ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
#     for spine in ax.spines.values():
#         spine.set_color("#334155")

#     return fig

# def yearly_profit(df, from_, to_):
#     # 1. Ensure DatetimeIndex before slicing/resampling
#     data = data_process(df)
#     yearly_data = data.loc[str(from_) : str(to_)]
#     profit = yearly_data["profit"].resample("YE").sum()

#     # 2. Setup Dark Theme & Figure
#     sns.set_theme(style="dark")
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
#     fig.patch.set_facecolor("#0E1117")
#     ax.set_facecolor("#161B22")

#     # 3. Line plot with neon-cyan accents
#     sns.lineplot(
#         x=profit.index,
#         y=profit.values,
#         ax=ax,
#         color="#3B82F6",  # Bright dark-mode blue
#         linewidth=2.5,
#         marker="o",
#         markersize=6,
#         markerfacecolor="#0E1117",
#         markeredgewidth=2,
#         markeredgecolor="#3B82F6",
#     )

#     # Shaded fill under the line
#     ax.fill_between(profit.index, profit.values, color="#00F2FE", alpha=0.15)

#     # 4. Title, Labels & Colors
#     ax.set_ylabel(
#         "Profit ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
#     )

#     # 5. Currency formatting on Y-axis
#     ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

#     # 6. Dark Mode Grid & Spine Styling
#     ax.tick_params(colors="#94A3B8", labelsize=9)
#     ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
#     for spine in ax.spines.values():
#         spine.set_color("#334155")

#     return fig

# def yearly_sales(df, from_, to_):
    # 1. Ensure DatetimeIndex before slicing/resampling
    data = data_process(df)
    yearly_data = data.loc[str(from_) : str(to_)]
    sales = yearly_data["sales"].resample("YE").sum()

    # 2. Setup Dark Theme & Figure
    sns.set_theme(style="dark")
    fig, ax = plt.subplots(figsize=(15, 8))

    # Dark mode backgrounds (matching Streamlit dark theme aesthetics)
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#161B22")

    # 3. Line plot with vibrant purple-blue accents
    sns.lineplot(
        x=sales.index,
        y=sales.values,
        ax=ax,
        color="#3B82F6",  # Bright dark-mode blue
        linewidth=2.5,
        marker="o",
        markersize=6,
        markerfacecolor="#0E1117",
        markeredgewidth=2,
        markeredgecolor="#3B82F6",
    )

    # Shaded fill under the line
    ax.fill_between(sales.index, sales.values, color="#3B82F6", alpha=0.15)

    # 4. Title, Labels & Colors
    ax.set_ylabel(
        "Sales ($)", fontsize=10, fontweight="bold", color="#E2E8F0"
    )

    # 5. Currency formatting on Y-axis
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.0f}"))

    # 6. Dark Mode Grid & Spine Styling
    ax.tick_params(colors="#94A3B8", labelsize=9)
    ax.grid(True, color="#334155", linestyle="--", linewidth=0.5, alpha=0.7)
    for spine in ax.spines.values():
        spine.set_color("#334155")

    return fig

def _apply_dark_theme(fig, title_text, y_label):
    """Helper function to apply consistent dark mode styling across all charts."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(
            showgrid=True, 
            gridcolor="#334155", 
            title=None,
            tickfont=dict(color="#94A3B8")
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor="#334155", 
            title=dict(text=y_label, font=dict(color="#E2E8F0", size=12)),
            tickprefix="$",
            tickfont=dict(color="#94A3B8")
        )
    )
    return fig


def monthly_profit(df, from_, to_):
    data = data_process(df)
    monthly_data = data.loc[str(from_) : str(to_)]
    profit = monthly_data["profit"].resample("ME").sum().reset_index()

    fig = px.line(
        profit,
        x="order-date",
        y="profit",
        markers=True,
    )

    fig.update_traces(
        line_color="#00A3AB",
        marker=dict(size=9, color="#00A3AB"),
        fill='tozeroy',
        fillcolor='rgba(0, 242, 254, 0.15)',
        hovertemplate="<b>Date:</b> %{x|%B %Y}<br><b>Profit:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Monthly Profit", "Profit ($)")

def monthly_sales(df, from_, to_):
    data = data_process(df)
    monthly_data = data.loc[str(from_) : str(to_)]
    sales = monthly_data["sales"].resample("ME").sum().reset_index()

    fig = px.line(
        sales,
        x="order-date",
        y="sales",
        markers=True,
    )

    fig.update_traces(
        line_color="#3B82F6",  # Bright Blue
        marker=dict(size=7, color="#3B82F6"),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.15)',
        hovertemplate="<b>Date:</b> %{x|%B %Y}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Monthly Sales", "Sales ($)")

def quarterly_profit(df, from_, to_):
    data = data_process(df)
    quarterly_data = data.loc[str(from_) : str(to_)]
    profit = quarterly_data["profit"].resample("QE").sum().reset_index()

    fig = px.line(
        profit,
        x="order-date",
        y="profit",
        markers=True,
    )

    fig.update_traces(
        line_color="#00A3AB",
        marker=dict(size=9, color="#00A3AB"),
        fill='tozeroy',
        fillcolor='rgba(0, 242, 254, 0.15)',
        hovertemplate="<b>Quarter:</b> %{x|Q%q %Y}<br><b>Profit:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Quarterly Profit", "Profit ($)")

def quarterly_sales(df, from_, to_):
    data = data_process(df)
    quarterly_data = data.loc[str(from_) : str(to_)]
    sales = quarterly_data["sales"].resample("QE").sum().reset_index()

    fig = px.line(
        sales,
        x="order-date",
        y="sales",
        markers=True,
    )

    fig.update_traces(
        line_color="#3B82F6",
        marker=dict(size=8, color="#3B82F6"),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.15)',
        hovertemplate="<b>Quarter:</b> %{x|Q%q %Y}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Quarterly Sales", "Sales ($)")

def yearly_profit(df, from_, to_):
    data = data_process(df)
    yearly_data = data.loc[str(from_) : str(to_)]
    profit = yearly_data["profit"].resample("YE").sum().reset_index()

    fig = px.line(
        profit,
        x="order-date",
        y="profit",
        markers=True,
    )

    fig.update_traces(
        line_color="#00A3AB",
        marker=dict(size=9, color="#00A3AB"),
        fill='tozeroy',
        fillcolor='rgba(0, 242, 254, 0.15)',
        hovertemplate="<b>Year:</b> %{x|%Y}<br><b>Profit:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Yearly Profit", "Profit ($)")

def yearly_sales(df, from_, to_):
    data = data_process(df)
    yearly_data = data.loc[str(from_) : str(to_)]
    sales = yearly_data["sales"].resample("YE").sum().reset_index()

    fig = px.line(
        sales,
        x="order-date",
        y="sales",
        markers=True,
    )

    fig.update_traces(
        line_color="#3B82F6",
        marker=dict(size=9, color="#3B82F6"),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.15)',
        hovertemplate="<b>Year:</b> %{x|%Y}<br><b>Sales:</b> $%{y:,.2f}<extra></extra>"
    )

    return _apply_dark_theme(fig, "Yearly Sales", "Sales ($)")


def monthly_quantity(df, from_, to_):
    data = data_process(df)
    monthly_data = data.loc[str(from_) : str(to_)]
    quantity = monthly_data["quantity"].resample("ME").sum().reset_index()

    fig = px.line(
        quantity,
        x="order-date",
        y="quantity",
        markers=True,
    )

    fig.update_traces(
        line_color="#A855F7",  # Vibrant Neon Purple
        marker=dict(size=7, color="#A855F7"),
        fill='tozeroy',
        fillcolor='rgba(168, 85, 247, 0.15)',
        hovertemplate="<b>Date:</b> %{x|%B %Y}<br><b>Quantity Sold:</b> %{y:,.0f} units<extra></extra>"
    )

    # Note: Custom y-axis formatting without '$' for raw counts
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=True, gridcolor="#334155", title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text="Quantity (Units)", font=dict(color="#E2E8F0", size=12)), tickfont=dict(color="#94A3B8"))
    )

    return fig

def quarterly_quantity(df, from_, to_):
    data = data_process(df)
    quarterly_data = data.loc[str(from_) : str(to_)]
    quantity = quarterly_data["quantity"].resample("QE").sum().reset_index()

    fig = px.line(
        quantity,
        x="order-date",
        y="quantity",
        markers=True,
    )

    fig.update_traces(
        line_color="#A855F7",
        marker=dict(size=8, color="#A855F7"),
        fill='tozeroy',
        fillcolor='rgba(168, 85, 247, 0.15)',
        hovertemplate="<b>Quarter:</b> %{x|Q%q %Y}<br><b>Quantity Sold:</b> %{y:,.0f} units<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=True, gridcolor="#334155", title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text="Quantity (Units)", font=dict(color="#E2E8F0", size=12)), tickfont=dict(color="#94A3B8"))
    )

    return fig

def yearly_quantity(df, from_, to_):
    data = data_process(df)
    quarterly_data = data.loc[str(from_) : str(to_)]
    quantity = quarterly_data["quantity"].resample("QE").sum().reset_index()

    fig = px.line(
        quantity,
        x="order-date",
        y="quantity",
        markers=True,
    )

    fig.update_traces(
        line_color="#A855F7",
        marker=dict(size=8, color="#A855F7"),
        fill='tozeroy',
        fillcolor='rgba(168, 85, 247, 0.15)',
        hovertemplate="<b>Quarter:</b> %{x|Q%q %Y}<br><b>Quantity Sold:</b> %{y:,.0f} units<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=True, gridcolor="#334155", title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text="Quantity (Units)", font=dict(color="#E2E8F0", size=12)), tickfont=dict(color="#94A3B8"))
    )

    return fig


def yearly_quantity(df, from_, to_):
    data = data_process(df)
    yearly_data = data.loc[str(from_) : str(to_)]
    quantity = yearly_data["quantity"].resample("YE").sum().reset_index()

    fig = px.line(
        quantity,
        x="order-date",
        y="quantity",
        markers=True,
    )

    fig.update_traces(
        line_color="#A855F7",
        marker=dict(size=9, color="#A855F7"),
        fill='tozeroy',
        fillcolor='rgba(168, 85, 247, 0.15)',
        hovertemplate="<b>Year:</b> %{x|%Y}<br><b>Quantity Sold:</b> %{y:,.0f} units<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=True, gridcolor="#334155", title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text="Quantity (Units)", font=dict(color="#E2E8F0", size=12)), tickfont=dict(color="#94A3B8"))
    )

    return fig

def day_wise_analysis(df, metric="profit"):
    """
    Groups data by Day of the Week (Monday - Sunday) 
    metric options: 'profit' or 'sales'
    """
    data = data_process(df)
    
    # Extract day name and define correct order
    data['day_name'] = data.index.day_name()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Aggregate metric
    df_day = data.groupby('day_name')[metric].sum().reindex(day_order).reset_index()

    # Define color scheme based on metric
    color = "#00A3AB" if metric == "profit" else "#3B82F6"
    hover_title = "Profit" if metric == "profit" else "Sales"

    fig = px.bar(
        df_day,
        x='day_name',
        y=metric,
        text_auto='.2s'
    )

    fig.update_traces(
        marker_color=color,
        hovertemplate=f"<b>Day:</b> %{{x}}<br><b>Total {hover_title}:</b> $%{{y:,.2f}}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(showgrid=False, title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text=f"Total {hover_title} ($)", font=dict(color="#E2E8F0")), tickprefix="$", tickfont=dict(color="#94A3B8"))
    )

    return fig

def month_wise_analysis(df, metric="profit"):
    """
    Groups data by Month of the Year (January - December)
    metric options: 'profit' or 'sales'
    """
    data = data_process(df)
    
    # Extract month name and define correct order
    data['month_name'] = data.index.month_name()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    # Aggregate metric
    df_month = data.groupby('month_name')[metric].sum().reindex(month_order).reset_index()

    # Define color scheme based on metric
    color = "#00A3AB" if metric == "profit" else "#3B82F6"
    hover_title = "Profit" if metric == "profit" else "Sales"

    fig = px.bar(
        df_month,
        x='month_name',
        y=metric,
        text_auto='.2s'
    )

    fig.update_traces(
        marker_color=color,
        hovertemplate=f"<b>Month:</b> %{{x}}<br><b>Total {hover_title}:</b> $%{{y:,.2f}}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(showgrid=False, title=None, tickfont=dict(color="#94A3B8")),
        yaxis=dict(showgrid=True, gridcolor="#334155", title=dict(text=f"Total {hover_title} ($)", font=dict(color="#E2E8F0")), tickprefix="$", tickfont=dict(color="#94A3B8"))
    )

    return fig