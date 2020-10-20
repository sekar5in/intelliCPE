# define constants.
VIR_CONNECT_LIST_DOMAINS_ACTIVE = 1
VIR_CONNECT_LIST_DOMAINS_INACTIVE = 2
VIR_CONNECT_LIST_DOMAINS_PERSISTENT = 4
VIR_CONNECT_LIST_DOMAINS_TRANSIENT = 8
VIR_CONNECT_LIST_DOMAINS_RUNNING = 16
VIR_CONNECT_LIST_DOMAINS_PAUSED = 32
VIR_CONNECT_LIST_DOMAINS_SHUTOFF = 64
VIR_CONNECT_LIST_DOMAINS_OTHER = 128
VIR_CONNECT_LIST_DOMAINS_MANAGEDSAVE = 256
VIR_CONNECT_LIST_DOMAINS_NO_MANAGEDSAVE = 512
VIR_CONNECT_LIST_DOMAINS_AUTOSTART = 1024
VIR_CONNECT_LIST_DOMAINS_NO_AUTOSTART = 2048
VIR_CONNECT_LIST_DOMAINS_HAS_SNAPSHOT = 4096
VIR_CONNECT_LIST_DOMAINS_NO_SNAPSHOT = 8192

"""
VIR_DOMAIN_NOSTATE = 0 # no state
VIR_DOMAIN_RUNNING = 1 # the domain is running
VIR_DOMAIN_BLOCKED = 2 # the domain is blocked on resource
VIR_DOMAIN_PAUSED = 3 # the domain is paused by user
VIR_DOMAIN_SHUTDOWN	= 4 # the domain is being shut down
VIR_DOMAIN_SHUTOFF = 5 # the domain is shut off
VIR_DOMAIN_CRASHED = 6 # the domain is crashed
VIR_DOMAIN_PMSUSPENDED = 7 # the domain is suspended by guest power management
VIR_DOMAIN_LAST = 8 # NB: this enum value will increase over time as new events are added to the libvirt API. It reflects the last state supported by this version of the libvirt API.
"""

VMSTATE = { 0 : "VIR_DOMAIN_NOSTATE",
1 : "VIR_DOMAIN_RUNNING",
2 : "VIR_DOMAIN_BLOCKED",
3 : "VIR_DOMAIN_PAUSED",
4 : "VIR_DOMAIN_SHUTDOWN",
5 : "VIR_DOMAIN_SHUTOFF",
6 : "VIR_DOMAIN_CRASHED",
7 : "VIR_DOMAIN_PMSUSPENDED",
8 : "VIR_DOMAIN_LAST"}


VMSTATUS = {
    0 : "INACTIVE",
    1 : "ACTIVE"
}

# virDomainShutdownReason
VIR_DOMAIN_SHUTDOWN_UNKNOWN	=	0 # (0x0)	the reason is unknown
VIR_DOMAIN_SHUTDOWN_USER	=	1 # (0x1)    shutting down on user request
VIR_DOMAIN_SHUTDOWN_LAST	=	2 # (0x2)

# virDomainShutoffReason
VIR_DOMAIN_SHUTOFF_UNKNOWN	=	0 # (0x0) the reason is unknown
VIR_DOMAIN_SHUTOFF_SHUTDOWN	=	1 # (0x1) normal shutdown
VIR_DOMAIN_SHUTOFF_DESTROYED =	2 # (0x2) forced poweroff
VIR_DOMAIN_SHUTOFF_CRASHED	=	3 # (0x3) domain crashed
VIR_DOMAIN_SHUTOFF_MIGRATED	=	4 # (0x4) migrated to another host
VIR_DOMAIN_SHUTOFF_SAVED	=	5 # (0x5) saved to a file
VIR_DOMAIN_SHUTOFF_FAILED	=	6 # (0x6) domain failed to start
VIR_DOMAIN_SHUTOFF_FROM_SNAPSHOT	=	7 #(0x7) restored from a snapshot which was taken while domain was shutoff
VIR_DOMAIN_SHUTOFF_DAEMON	=	8 # (0x8) daemon decides to kill domain during reconnection processing
VIR_DOMAIN_SHUTOFF_LAST	=	9 # (0x9)

# virDomainRunningReason
VIR_DOMAIN_RUNNING_UNKNOWN	=	0 # (0x0)
VIR_DOMAIN_RUNNING_BOOTED	=	1 # (0x1) normal startup from boot
VIR_DOMAIN_RUNNING_MIGRATED	=	2 # (0x2) migrated from another host
VIR_DOMAIN_RUNNING_RESTORED	=	3 # (0x3) restored from a state file
VIR_DOMAIN_RUNNING_FROM_SNAPSHOT =	4 # (0x4) restored from snapshot
VIR_DOMAIN_RUNNING_UNPAUSED	=	5 # (0x5) returned from paused state
VIR_DOMAIN_RUNNING_MIGRATION_CANCELED	=	6 # (0x6) returned from migration
VIR_DOMAIN_RUNNING_SAVE_CANCELED	=	7 # (0x7) returned from failed save process
VIR_DOMAIN_RUNNING_WAKEUP	=	8 # (0x8) returned from pmsuspended due to wakeup event
VIR_DOMAIN_RUNNING_CRASHED	=	9 # (0x9) resumed from crashed
VIR_DOMAIN_RUNNING_POSTCOPY	=	10 # (0xa) running in post-copy migration mode
VIR_DOMAIN_RUNNING_LAST	=	11 #(0xb)

# virDomainPMSuspendedReason
VIR_DOMAIN_PMSUSPENDED_UNKNOWN	=	0 #(0x0)
VIR_DOMAIN_PMSUSPENDED_LAST	=	1 #(0x1)

# virDomainPausedReason
VIR_DOMAIN_PAUSED_UNKNOWN	=	0 # (0x0) the reason is unknown
VIR_DOMAIN_PAUSED_USER	=	1 # (0x1) paused on user request
VIR_DOMAIN_PAUSED_MIGRATION	=	2 # (0x2) paused for offline migration
VIR_DOMAIN_PAUSED_SAVE	=	3 # (0x3) paused for save
VIR_DOMAIN_PAUSED_DUMP	=	4 # (0x4) paused for offline core dump
VIR_DOMAIN_PAUSED_IOERROR	=	5 # (0x5) paused due to a disk I/O error
VIR_DOMAIN_PAUSED_WATCHDOG	=	6 # (0x6) paused due to a watchdog event
VIR_DOMAIN_PAUSED_FROM_SNAPSHOT	=	7 # (0x7) paused after restoring from snapshot
VIR_DOMAIN_PAUSED_SHUTTING_DOWN	=	8 # (0x8) paused during shutdown process
VIR_DOMAIN_PAUSED_SNAPSHOT	=	9 # (0x9) paused while creating a snapshot
VIR_DOMAIN_PAUSED_CRASHED	=	10 # (0xa) paused due to a guest crash
VIR_DOMAIN_PAUSED_STARTING_UP	=	11 # (0xb) the domain is being started
VIR_DOMAIN_PAUSED_POSTCOPY	=	12 # (0xc) paused for post-copy migration
VIR_DOMAIN_PAUSED_POSTCOPY_FAILED	=	13 # (0xd) paused after failed post-copy
VIR_DOMAIN_PAUSED_LAST	=	14 # (0xe)

# virDomainNostateReason
VIR_DOMAIN_NOSTATE_UNKNOWN	=	0 # (0x0)
VIR_DOMAIN_NOSTATE_LAST	=	1 # (0x1)

# virDomainCrashedReason
VIR_DOMAIN_CRASHED_UNKNOWN	=	0 # (0x0) crashed for unknown reason
VIR_DOMAIN_CRASHED_PANICKED	=	1 # (0x1)	domain panicked
VIR_DOMAIN_CRASHED_LAST	=	2 # (0x2)

# virDomainBlockedReason
VIR_DOMAIN_BLOCKED_UNKNOWN	=	0 # (0x0) the reason is unknown
VIR_DOMAIN_BLOCKED_LAST	=	1 # (0x1)

