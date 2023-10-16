# OT2 Normalisation

This system can be used to normalise a plate of samples based on a csv of concentrations and volumes.

## First-time Setup

1. Download this repository and navigate to it

2. Get the wired IP address of the OT2 using the Opentrons app (more information here: [Setting up SSH access to your OT-2](https://support.opentrons.com/s/article/Setting-up-SSH-access-to-your-OT-2))

3. Run `bash setup.sh [ot2 ip]` which will generate a public/private key pair and upload the public key to the OT2. Use of a password is optional.

4. Import norm.py or norm_no_mix.py as a protocol using the Opentrons app. 
   (the only difference is that norm_no_mix.py does minimum mixing, which speeds up the run but means you will need to mix the plate yourself, e.g. vortexing)

## OT2 Setup

#### Pipettes

Single-channel P20: Right side

Single-channel P300: Left side

#### Deck

**Slot 1**: Source/sample plate (Bio-rad Hard-Shell 96W Low Skrtd Wht/Clr - HSP9601) 

**Slot 2**: Empty plate for normalised samples (Bio-rad Hard-Shell 96W Low Skrtd Wht/Clr - HSP9601)

**Slot 4**: 50 mL Falcon tube with 50 mL of diluent in A1 position of opentrons 6-tube-rack

**Pipette-tip boxes**: As described in Opentrons app after selecting "Start setup", this will vary based on the number of samples.

## Useage

1. Ensure OT2 is switched on

2. If needed, change pipettes to the configuration in 'OT2 Setup'

3. Prepare csv file containing dilution information (following the format of norm_csv.csv). The information for each well must be in the order of A1-H1, A2-H2, A3-H3 etc.

4. Get the IP address (wired or wireless) of the OT2 using the Opentrons app

5. Run `bash transfer_csv.sh [csv path] [ot2 ip]`

6. 'Start setup' on the protocol in the Opentrons app

7. Set up the deck as described in 'OT2 Setup' and in the Opentrons app

8. You can now run the protocol



---



Things to change:

calculate number of tips needed based on which tip will be used for each sample
