# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device find5
%define vendor oppo

%define rpm_device find5
%define rpm_vendor oppo

%define vendor_pretty OPPO
%define device_pretty Find5

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 2.0

# We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs
Provides: sensord-configs

%include droid-configs-device/droid-configs.inc

