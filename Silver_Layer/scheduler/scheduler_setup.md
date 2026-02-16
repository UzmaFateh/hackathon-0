# Scheduler Setup - Silver Tier

## Overview

This guide explains how to schedule Silver Layer components to run automatically.

## Components to Schedule

1. **Gmail Watcher** - Check for new emails every 5 minutes
2. **LinkedIn Watcher** - Check for engagement every 10 minutes
3. **Plan Engine** - Process new tasks every 15 minutes
4. **Approval Flow** - Check for approvals every 1 minute

---

## Windows Task Scheduler

### Setup Gmail Watcher

1. Open Task Scheduler (`taskschd.msc`)
2. Click "Create Basic Task"
3. Name: `AI Employee - Gmail Watcher`
4. Trigger: `At startup`
5. Action: `Start a program`
   - Program: `pythonw.exe` (runs without console window)
   - Arguments: `Silver_Layer\watchers\gmail_watcher.py`
   - Start in: `C:\path\to\AI_Employee_Vault_Bronze_Stable`
6. Finish and enable the task

### Setup LinkedIn Watcher

Repeat above steps with:
- Name: `AI Employee - LinkedIn Watcher`
- Arguments: `Silver_Layer\watchers\linkedin_watcher.py`

### Setup Plan Engine

Repeat above steps with:
- Name: `AI Employee - Plan Engine`
- Arguments: `Silver_Layer\reasoning\plan_engine.py --continuous`

### Setup Approval Flow

Repeat above steps with:
- Name: `AI Employee - Approval Flow`
- Arguments: `Silver_Layer\approval\approval_flow.py --continuous`

### Quick PowerShell Script

Save as `start_silver_layer.ps1`:

```powershell
# Start all Silver Layer components
$vaultPath = "C:\path\to\AI_Employee_Vault_Bronze_Stable"

Start-Process pythonw -ArgumentList "$vaultPath\Silver_Layer\watchers\gmail_watcher.py" -WorkingDirectory $vaultPath
Start-Process pythonw -ArgumentList "$vaultPath\Silver_Layer\watchers\linkedin_watcher.py" -WorkingDirectory $vaultPath
Start-Process pythonw -ArgumentList "$vaultPath\Silver_Layer\reasoning\plan_engine.py --continuous" -WorkingDirectory $vaultPath
Start-Process pythonw -ArgumentList "$vaultPath\Silver_Layer\approval\approval_flow.py --continuous" -WorkingDirectory $vaultPath

Write-Host "Silver Layer components started"
```

Run at startup:
1. Press `Win + R`
2. Type `shell:startup`
3. Create shortcut to `start_silver_layer.ps1`

---

## Mac/Linux - Cron

### Edit Crontab

```bash
crontab -e
```

### Add Cron Jobs

```bash
# Gmail Watcher - every 5 minutes
*/5 * * * * cd /path/to/AI_Employee_Vault_Bronze_Stable && python3 Silver_Layer/watchers/gmail_watcher.py >> Silver_Layer/logs/gmail_watcher.log 2>&1

# LinkedIn Watcher - every 10 minutes
*/10 * * * * cd /path/to/AI_Employee_Vault_Bronze_Stable && python3 Silver_Layer/watchers/linkedin_watcher.py >> Silver_Layer/logs/linkedin_watcher.log 2>&1

# Plan Engine - every 15 minutes
*/15 * * * * cd /path/to/AI_Employee_Vault_Bronze_Stable && python3 Silver_Layer/reasoning/plan_engine.py >> Silver_Layer/logs/plan_engine.log 2>&1

# Approval Flow - every minute
* * * * * cd /path/to/AI_Employee_Vault_Bronze_Stable && python3 Silver_Layer/approval/approval_flow.py >> Silver_Layer/logs/approval_flow.log 2>&1
```

### Using systemd (Linux)

Create service files in `/etc/systemd/system/`:

**gmail-watcher.service:**
```ini
[Unit]
Description=AI Employee Gmail Watcher
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/AI_Employee_Vault_Bronze_Stable
ExecStart=/usr/bin/python3 Silver_Layer/watchers/gmail_watcher.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable gmail-watcher
sudo systemctl start gmail-watcher
sudo systemctl status gmail-watcher
```

Repeat for other components.

---

## Mac - launchd

Create plist files in `~/Library/LaunchAgents/`:

**com.aiemployee.gmail-watcher.plist:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.aiemployee.gmail-watcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/AI_Employee_Vault_Bronze_Stable/Silver_Layer/watchers/gmail_watcher.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/AI_Employee_Vault_Bronze_Stable</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/path/to/AI_Employee_Vault_Bronze_Stable/Silver_Layer/logs/gmail_watcher.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/AI_Employee_Vault_Bronze_Stable/Silver_Layer/logs/gmail_watcher_error.log</string>
</dict>
</plist>
```

Load the service:
```bash
launchctl load ~/Library/LaunchAgents/com.aiemployee.gmail-watcher.plist
```

---

## Manual Start (All Platforms)

### Start All Components

**Windows:**
```cmd
cd C:\path\to\AI_Employee_Vault_Bronze_Stable
start pythonw Silver_Layer\watchers\gmail_watcher.py
start pythonw Silver_Layer\watchers\linkedin_watcher.py
start pythonw Silver_Layer\reasoning\plan_engine.py --continuous
start pythonw Silver_Layer\approval\approval_flow.py --continuous
```

**Mac/Linux:**
```bash
cd /path/to/AI_Employee_Vault_Bronze_Stable
python3 Silver_Layer/watchers/gmail_watcher.py &
python3 Silver_Layer/watchers/linkedin_watcher.py &
python3 Silver_Layer/reasoning/plan_engine.py --continuous &
python3 Silver_Layer/approval/approval_flow.py --continuous &
```

### Stop All Components

**Windows:**
```cmd
taskkill /F /IM pythonw.exe
```

**Mac/Linux:**
```bash
pkill -f "gmail_watcher.py"
pkill -f "linkedin_watcher.py"
pkill -f "plan_engine.py"
pkill -f "approval_flow.py"
```

---

## Recommended Schedule

| Component | Frequency | Reason |
|-----------|-----------|--------|
| Gmail Watcher | Every 5 min | Balance between responsiveness and API limits |
| LinkedIn Watcher | Every 10 min | LinkedIn has stricter rate limits |
| Plan Engine | Every 15 min | Tasks don't need immediate planning |
| Approval Flow | Every 1 min | Quick response to human approvals |

---

## Monitoring

### Check if Components are Running

**Windows:**
```cmd
tasklist | findstr pythonw
```

**Mac/Linux:**
```bash
ps aux | grep python | grep Silver_Layer
```

### View Logs

All components log to `Silver_Layer/logs/`:
- `gmail_watcher_YYYY-MM-DD.log`
- `linkedin_watcher_YYYY-MM-DD.log`
- `plan_engine_YYYY-MM-DD.log`
- `approval_flow_YYYY-MM-DD.log`

**Tail logs in real-time:**
```bash
tail -f Silver_Layer/logs/*.log
```

---

## Troubleshooting

### Components Not Starting

1. Check Python is in PATH
2. Verify working directory is correct
3. Check file permissions
4. Review error logs

### High CPU Usage

1. Increase check intervals in config files
2. Reduce number of concurrent watchers
3. Check for infinite loops in logs

### Missing Logs

1. Ensure `Silver_Layer/logs/` directory exists
2. Check write permissions
3. Verify log paths in scripts

---

## Production Recommendations

1. **Use systemd/launchd** for reliability (auto-restart on failure)
2. **Monitor logs** regularly for errors
3. **Set up alerts** for component failures
4. **Rotate logs** to prevent disk space issues
5. **Test scheduling** before production deployment

---

## Log Rotation (Optional)

**Linux logrotate config** (`/etc/logrotate.d/ai-employee`):
```
/path/to/AI_Employee_Vault_Bronze_Stable/Silver_Layer/logs/*.log {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
}
```
