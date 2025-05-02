# Multipath TCP Test Environment Setup Guideline

## Introduction

**Multipath TCP (MPTCP)** enhances TCP by allowing multiple paths to maximize resource usage and increase redundancy. This guideline is focusing teach you how to configure the environment and test the performance of it.

## Setup

### Server

In order to establish the MPTCP connection between Server and Client, we need to set up a cloud server with public IP address.

1. Install the system which support MPTCP. We are running Ubuntu 24.04.2 LTS here.

2. Install the essential tools we need:

   - iperf3
   - mptcpize

3. Enable MPTCP on Ubuntu, MPTCP is default enabled on most of the Linux distribution now. You can the following command to enable it.

   ```shell
   sudo sysctl -w net.mptcp.enabled=1 
   ```

### Client

Enable multiple network interface on the client side. It's essential to establish subflows while using MPTCP

1. Using the latest Ubuntu LTS version. 
2. Install the tools:
   - iperf3
   - mptcpize

## Test

Before establish the MPTCP connection, use the following command to start a MPTCP connection monitor:

```shell
sudo ip mptcp monitor
```

Use the following commands to start iperf3 on **Server**(mptcpize run...is for force the connection use MPTCP protocol).

```shell
mptcpize run iperf3 -s
```

And the following commands on **Client**

```shell
mptcpize run iperf3 -c "Server IP"
```

In addition, we can also use Wireshark to monitor the specific packets information of MPTCP connection.

