"use client";

// MetricsBar is rendered inline in page.tsx as part of the dashboard layout.
// This file is a placeholder export in case you want to extract it later.

interface MetricProps {
  pending: number;
  accepted: number;
  avgResponseSeconds: number;
  ambulancesAvailable: number;
  ambulancesTotal: number;
}

export default function MetricsBar({
  pending,
  accepted,
  avgResponseSeconds,
  ambulancesAvailable,
  ambulancesTotal,
}: MetricProps) {
  return (
    <div className="metrics-bar">
      <div className="metric-cell">
        <div className="metric-label">Pending SOS</div>
        <div className="metric-value red">{String(pending).padStart(2, "0")}</div>
        <div className="metric-sub">Awaiting response</div>
      </div>
      <div className="metric-cell">
        <div className="metric-label">Accepted</div>
        <div className="metric-value green">{String(accepted).padStart(2, "0")}</div>
        <div className="metric-sub">Ambulance dispatched</div>
      </div>
      <div className="metric-cell">
        <div className="metric-label">Ambulances Available</div>
        <div className="metric-value amber">{String(ambulancesAvailable).padStart(2, "0")}</div>
        <div className="metric-sub">of {ambulancesTotal} units</div>
      </div>
      <div className="metric-cell">
        <div className="metric-label">Avg Response Time</div>
        <div className="metric-value blue">{avgResponseSeconds}s</div>
        <div className="metric-sub">Target: &lt;30s ✓</div>
      </div>
    </div>
  );
}
