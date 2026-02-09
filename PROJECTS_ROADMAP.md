# SOC Analyst Projects Roadmap

Hands-on cybersecurity projects to demonstrate practical SOC analyst capabilities. Each project takes 2-4 hours and focuses on real-world security operations skills.

## Completed Projects

- [x] **Vulnerable Login Application with Interactive Dashboard** (February 2026)
  - Intentionally vulnerable Flask app for studying authentication attacks
  - Interactive dashboard with live attack simulations
  - Real-time log analysis and pattern detection
  - Demonstrates: Web security, Python development, attack simulation, log analysis
  - Live demo: [jasonklutts.com/lab](https://jasonklutts.com/lab)
  - Code: [GitHub](https://github.com/jasonklutts/vulnerable-login-lab)

---

## Network Analysis & Monitoring

- [ ] **Port Scanner with Service Detection**
  - Python script scanning target IPs for open ports
  - Identifies running services and versions
  - JSON output for SIEM ingestion
  - Skills: Network reconnaissance, service enumeration, Python scripting

- [ ] **Packet Capture Analysis Automation**
  - Reads PCAP files and extracts suspicious indicators
  - Flags anomalies: port scanning, failed connections, unusual protocols
  - Generates summary reports with statistics
  - Skills: Network forensics, packet analysis, threat detection

- [ ] **Network Baseline Monitor**
  - Captures normal traffic patterns over 24 hours
  - Alerts on deviations: unusual ports, new IPs, traffic spikes
  - Simple anomaly detection implementation
  - Skills: Behavioral analysis, baseline establishment, anomaly detection

---

## Log Analysis & SIEM

- [ ] **Failed Login Analyzer**
  - Parses auth.log or Windows Event logs
  - Identifies brute force patterns and suspicious source IPs
  - Outputs IOCs for blocking
  - Skills: Log parsing, pattern recognition, IOC generation

- [ ] **Log Correlation Script**
  - Ingests logs from multiple sources (firewall, IDS, auth)
  - Correlates events by timestamp and source IP
  - Identifies multi-stage attack patterns
  - Skills: Log correlation, incident investigation, multi-source analysis

- [ ] **Syslog Parser with Alert Rules**
  - Monitors live syslog feed for configurable keywords
  - Triggers alerts on suspicious patterns
  - Sends notifications via email or webhook
  - Skills: Real-time monitoring, alert configuration, automation

---

## Threat Intelligence & IOC Management

- [ ] **IOC Checker Against Live Systems**
  - Checks known malicious IPs/domains/hashes against live systems
  - Searches firewall logs, DNS queries, running processes
  - Reports matches with context
  - Skills: Threat intelligence application, IOC validation, system analysis

- [ ] **Automated Threat Feed Aggregator**
  - Pulls IOCs from public feeds (AlienVault OTX, abuse.ch)
  - Deduplicates and formats for import
  - Daily updates with historical tracking
  - Skills: Threat intelligence, API integration, data processing

- [ ] **Domain Reputation Checker**
  - Analyzes domains for age, SSL status, DNS records
  - Checks against threat intelligence sources
  - Flags newly registered or suspicious domains
  - Skills: Phishing detection, OSINT, domain analysis

---

## Incident Response Tools

- [ ] **Automated Evidence Collection Script**
  - Gathers forensic artifacts from compromised systems
  - Collects: processes, connections, scheduled tasks, recent files
  - Outputs timeline and artifact package
  - Skills: Incident response, forensic collection, evidence preservation

- [ ] **Alert Triage Dashboard**
  - Web interface for queued security alerts
  - Categorization: true positive, false positive, needs investigation
  - Tracks MTTD and MTTR metrics
  - Skills: Alert triage, workflow management, metrics tracking

- [ ] **Process Monitor with Baseline Comparison**
  - Captures running processes and compares to known-good baseline
  - Flags new or suspicious processes
  - Checks hashes against VirusTotal API
  - Skills: Host-based detection, baseline comparison, threat analysis

---

## Vulnerability & Compliance

- [ ] **Web Application Header Scanner**
  - Checks websites for missing security headers
  - Tests for misconfigurations (CORS, CSP, HSTS)
  - Generates remediation recommendations
  - Skills: Web security, vulnerability assessment, secure configuration

- [ ] **Password Policy Auditor**
  - Analyzes password hashes from test environment
  - Identifies weak passwords using wordlists
  - Reports on policy compliance
  - Skills: Access control, password security, policy enforcement

- [ ] **Open Share Enumeration Tool**
  - Scans network for open SMB shares
  - Identifies world-readable or writable shares
  - Lists exposed sensitive files
  - Skills: Lateral movement awareness, network enumeration, access control

---

## Priority Order (Recommended)

### Quick Wins (Start Here)
1. Failed Login Analyzer - Complements existing vulnerable login app
2. Port Scanner with Service Detection - Classic SOC reconnaissance tool
3. Domain Reputation Checker - Immediate threat intel value

### Medium Priority
4. Web Application Header Scanner - Quick security audit tool
5. IOC Checker Against Live Systems - Practical threat detection
6. Automated Evidence Collection Script - Core IR capability

### Advanced Projects
7. Log Correlation Script - More complex multi-source analysis
8. Alert Triage Dashboard - Full web application build
9. Network Baseline Monitor - Requires extended data collection

---

## Skills Matrix

| Project | Python | Web Dev | Network | Logs | Threat Intel | IR |
|---------|--------|---------|---------|------|--------------|-----|
| Vulnerable Login App | ✓ | ✓ | | ✓ | | |
| Port Scanner | ✓ | | ✓ | | | |
| Failed Login Analyzer | ✓ | | | ✓ | | |
| Domain Reputation | ✓ | | | | ✓ | |
| Evidence Collection | ✓ | | | | | ✓ |
| Alert Triage Dashboard | ✓ | ✓ | | ✓ | | |
| IOC Checker | ✓ | | | | ✓ | |

---

## Notes

- All projects include full documentation and source code
- Each demonstrates hands-on SOC analyst capabilities
- Projects are designed to be portfolio-ready
- Code will be hosted on GitHub with detailed README files
- Live demos hosted where applicable on jasonklutts.com

**Last Updated:** February 2026
