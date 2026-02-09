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

- [ ] **Failed Login Analyzer** ⭐ NEXT
  - Parses auth.log or Windows Event logs
  - Identifies brute force patterns and suspicious source IPs
  - Outputs IOCs for blocking
  - Skills: Log parsing, pattern recognition, IOC generation

- [ ] **Log Correlation Script**
  - Ingests logs from multiple sources (firewall, IDS, auth)
  - Correlates events by timestamp and source IP
  - Identifies multi-stage attack patterns
  - Skills: Log correlation, incident investigation, multi-source analysis

- [x] ~~**Syslog Parser with Alert Rules**~~ - Redundant with ELK Stack project

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

- [x] ~~**Alert Triage Dashboard**~~ - Redundant with SOC Dashboards project

- [x] ~~**Process Monitor with Baseline Comparison**~~ - Redundant with Adversary Simulation Lab

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

## Recommended Build Order

### Phase 1: Quick Wins & Skill Diversification (Weeks 1-2)

**Priority projects that complement existing portfolio:**

1. **Failed Login Analyzer** ⭐ NEXT
   - Extends vulnerable login app work
   - New skill: Windows Event Log parsing
   - Direct SOC triage application
   - Est. time: 2-3 hours

2. **Domain Reputation Checker**
   - Threat intelligence focus (new area)
   - WHOIS, DNS analysis, API integration
   - Phishing detection capability
   - Est. time: 3-4 hours

3. **Port Scanner with Service Detection**
   - Classic reconnaissance tool
   - Socket programming, banner grabbing
   - Network enumeration skills
   - Est. time: 2-3 hours

### Phase 2: Threat Intelligence Focus (Weeks 3-4)

4. **Automated Threat Feed Aggregator**
   - Proactive threat hunting
   - API integration, data normalization
   - Threat intel lifecycle demonstration
   - Est. time: 4-5 hours

5. **IOC Checker Against Live Systems**
   - Applies threat intel to infrastructure
   - Cross-references IOCs with logs
   - Practical detection capability
   - Est. time: 3-4 hours

### Phase 3: Advanced Analysis Tools (Weeks 5-6)

6. **Web Application Header Scanner**
   - OWASP Top 10 knowledge
   - HTTP security headers, secure config
   - Quick security audit capability
   - Est. time: 2-3 hours

7. **Automated Evidence Collection Script**
   - Incident response focus
   - Forensic artifact collection
   - Shows IR readiness
   - Est. time: 4-5 hours

8. **Log Correlation Script**
   - Advanced multi-source analysis
   - Timeline correlation
   - Investigation methodology
   - Est. time: 5-6 hours

### Projects Skipped

**Redundant with existing portfolio projects:**
- ~~Process Monitor with Baseline Comparison~~ - Covered by Adversary Simulation Lab
- ~~Alert Triage Dashboard~~ - Covered by SOC Dashboards with ELK Stack
- ~~Syslog Parser with Alert Rules~~ - Covered by ELK Stack implementation

---

## Skills Matrix

| Project | Python | Web Dev | Network | Logs | Threat Intel | IR |
|---------|--------|---------|---------|------|--------------|-----|
| Vulnerable Login App ✓ | ✓ | ✓ | | ✓ | | |
| Failed Login Analyzer | ✓ | | | ✓ | | |
| Domain Reputation | ✓ | | | | ✓ | |
| Port Scanner | ✓ | | ✓ | | | |
| Threat Feed Aggregator | ✓ | | | | ✓ | |
| IOC Checker | ✓ | | | ✓ | ✓ | |
| Header Scanner | ✓ | ✓ | | | | |
| Evidence Collection | ✓ | | | | | ✓ |
| Log Correlation | ✓ | | | ✓ | | ✓ |

---

## Repository Structure

Each project will have its own GitHub repository with:
- Detailed README with usage instructions
- Complete source code with comments
- Sample output and screenshots
- Documentation of lessons learned
- Links from jasonklutts.com portfolio

---

## Notes

- All projects include full documentation and source code
- Each demonstrates hands-on SOC analyst capabilities
- Projects are designed to be portfolio-ready
- Code hosted on GitHub with detailed README files
- Live demos hosted where applicable on jasonklutts.com
- Projects focus on filling skill gaps not covered by existing portfolio

**Last Updated:** February 9, 2026
