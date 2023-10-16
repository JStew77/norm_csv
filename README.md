# OT2 Normalisation

This system can be used to normalise a plate of samples based on a csv of concentrations and volumes.

## First-time Setup

1. Download this repository and navigate to it

2. Connect to the OT2 via a wired connection and get the wired IP address using the Opentrons app (more information here: [Opentrons Help Center](https://support.opentrons.com/s/article/Setting-up-SSH-access-to-your-OT-2))

3. Run `ssh-keygen -f ot2_ssh_key` to generate a public/private key pair. Use of a password is optional.

4. Run `bash public_key_upload.sh [public key path] [ot2 ip]`

5. Import norm.py or norm_no_mix.py as a protocol using the Opentrons app. 
   (the only difference is that norm_no_mix.py does minimum mixing, which speeds up the run but means you will need to mix the plate yourself, e.g. vortexing)

## OT2 Setup

##### Pipettes

Single-channel P20: Right side

Single-channel P300: Left side

##### Deck

**Slot 1**: Source/sample plate (Bio-rad Hard-Shell 96W Low Skrtd Wht/Clr - HSP9601) 

**Slot 2**: Empty plate for normalised samples (Bio-rad Hard-Shell 96W Low Skrtd Wht/Clr - HSP9601)

**Slot 4**: 50 mL Falcon tube with 50 mL of diluent in A1 position of opentrons 6-tube-rack

**Pipette-tip boxes**: As described in Opentrons app after selecting "Start setup", this will vary based on the number of samples.

## Useage

1. Ensure OT2 is switched on

2. If needed, change pipettes to the configuration in 'OT2 Setup'

3. Prepare csv file containing dilution information (following the format of norm_csv.csv)

4. Get the IP address (wired or wireless) of the OT2 using the Opentrons app

5. Run `bash transfer_csv.sh [csv path] [ot2 ip] [private key path]`

6. 'Start setup' on the protocol in the Opentrons app

7. Set up the deck as described in 'OT2 Setup' and in the Opentrons app

8. You can now run the protocol





Things to change:

calculate number of tips needed based on which tip will be used for each sample


