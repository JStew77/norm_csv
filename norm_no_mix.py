# def get_values(*names):
#     import json
#     _all_values = json.loads("""{"vol_water":50,"src_plate":"nest_96_wellplate_100ul_pcr_full_skirt","dst_plate":"nest_96_wellplate_100ul_pcr_full_skirt","p20_mount":"right","file_input":"Well,nanograms,sample volume,goal concentration,normalized volume\\nA1,5,30,2,30\\nB1,6,30,3,30\\nC1,7,30,4,30\\nD1,8,30,5,30\\nE1,9,30,6,30\\nF1,10,30,7,30\\nG1,11,30,8,30\\nH1,12,30,9,30\\nA2,13,30,10,30\\nB2,14,30,11,30\\nC2,15,30,12,30\\nD2,16,30,13,30\\nE2,17,30,14,30\\nF2,18,30,15,30\\nG2,19,30,16,30\\nH2,20,30,17,30\\nA3,21,30,18,30\\nB3,22,30,19,30\\nC3,23,30,20,30\\nD3,24,30,21,30\\nE3,25,30,22,30\\nF3,26,30,23,30\\nG3,27,30,24,30\\nH3,28,30,25,30\\nA4,29,30,26,30\\nB4,30,30,27,30\\nC4,31,30,28,30\\nD4,32,30,29,30\\nE4,33,30,30,30\\nF4,34,30,31,30\\nG4,35,30,32,30\\nH4,36,30,33,30\\nA5,37,30,34,30\\nB5,38,30,35,30\\nC5,39,30,36,30\\nD5,40,30,37,30\\nE5,41,30,38,30\\nF5,42,30,39,30\\nG5,43,30,40,30\\nH5,44,30,41,30\\nA6,45,30,42,30\\nB6,46,30,43,30\\nC6,47,30,44,30\\nD6,48,30,45,30\\nE6,49,30,46,30\\nF6,50,30,47,30\\nG6,51,30,48,30\\nH6,52,30,49,30\\nA7,53,30,50,30\\nB7,54,30,51,30\\nC7,55,30,52,30\\nD7,56,30,53,30\\nE7,57,30,54,30\\nF7,58,30,55,30\\nG7,59,30,56,30\\nH7,60,30,57,30\\nA8,61,30,58,30\\nB8,62,30,59,30\\nC8,63,30,60,30\\nD8,64,30,61,30\\nE8,65,30,62,30\\nF8,66,30,63,30\\nG8,67,30,64,30\\nH8,68,30,65,30\\nA9,69,30,66,30\\nB9,70,30,67,30\\nC9,71,30,68,30\\nD9,72,30,69,30\\nE9,73,30,70,30\\nF9,74,30,71,30\\nG9,75,30,72,30\\nH9,76,30,73,30\\nA10,77,30,74,30\\nB10,78,30,75,30\\nC10,79,30,76,30\\nD10,80,30,77,30\\nE10,81,30,78,30\\nF10,82,30,79,30\\nG10,83,30,80,30\\nH10,84,30,81,30\\nA11,85,30,82,30\\nB11,86,30,83,30\\nC11,87,30,84,30\\nD11,88,30,85,30\\nE11,89,30,86,30\\nF11,90,30,87,30\\nG11,91,30,88,30\\nH11,92,30,89,30\\nA12,93,30,90,30\\nB12,94,30,91,30\\nC12,95,30,92,30\\nD12,96,30,93,30\\nE12,97,30,94,30\\nF12,98,30,95,30\\nG12,99,30,96,30\\nH12,100,30,97,30"}""")
#     return [_all_values[n] for n in names]


"""OPEN TRONS."""
import math
import os
from pathlib import Path

metadata = {
    'protocolName': 'Normalization-csv upload, no mix',
    'author': 'Opentrons <protocols@opentrons.com>',
    'apiLevel': '2.12'
}

with open(os.path.join("/data/user_storage", "norm_csv.csv"), "r") as f:
    file_input = f.read()

def run(ctx):
    """PROTOCOL."""
    vol_water = 50
    src_plate = "biorad_96_wellplate_200ul_pcr"
    dst_plate = "biorad_96_wellplate_200ul_pcr"
    p20_mount = "right"

    # [vol_water, src_plate, dst_plate,
    #  p20_mount, file_input] = get_values(  # noqa: F821
    #     'vol_water', 'src_plate', 'dst_plate', 'p20_mount', 'file_input')

    if p20_mount == 'right':
        p300_mount = 'left'
    else:
        p300_mount = 'right'
    source_plate = ctx.load_labware(src_plate, '1', "source")
    dest_plate = ctx.load_labware(dst_plate, '2', "normalised")
    reagent_tubes = ctx.load_labware('opentrons_6_tuberack_'
                                     'falcon_50ml_conical', '4', "diluent")

    # parse
    csv_1 = file_input.split('\n')
    csv_2 = [val.split(',') for val in csv_1]
    header_removed = csv_2[1:]
    flat_list = [item for sublist in header_removed for item in sublist]
    well_list = flat_list[::4]
    start_conc = [eval(i) for i in flat_list[1::4]]
    final_conc = [eval(i) for i in flat_list[2::4]]
    final_vol = [eval(i) for i in flat_list[3::4]]
    bad_wells = []
    print(well_list)

    transfer_vol = []
    nfw_vol = []
    for final, start, vol in zip(final_conc, start_conc, final_vol):
        if start <= 0:
            transfer_vol.append(0)
        else:
            transfer_vol.append(round(vol * (final / start), 2))
    for s_vol, f_vol in zip(transfer_vol, final_vol):
        nfw_vol.append(f_vol - s_vol)
    lists = [well_list, final_vol,
             start_conc, final_conc, transfer_vol, nfw_vol]
    # clean up bad wells from lists
    for i, (start, final) in enumerate(zip(start_conc, final_conc)):
        if start < final:
            bad_wells.append(well_list[i])
            for list in lists:
                del list[i]
    # csv_2 = [val.split(',') for val in csv_1]
    # header_removed = csv_2[1:]
    # flat_list = [item for sublist in header_removed for item in sublist]
    # well_list = flat_list[::5]
    # sample_mass = [eval(i) for i in flat_list[1::5]]
    # sample_vol = [eval(i) for i in flat_list[2::5]]
    # final_mass = [eval(i) for i in flat_list[3::5]]
    # final_vol = [eval(i) for i in flat_list[4::5]]
    # start_conc = []
    # final_conc = []
    # bad_wells = []
    # print(well_list)
    #
    # for mass, vol in zip(sample_mass, sample_vol):
    #     start_conc.append(mass/vol)
    #
    # for mass, vol in zip(final_mass, final_vol):
    #     final_conc.append(mass/vol)
    #
    # transfer_vol = []
    # nfw_vol = []
    # for final, start, vol in zip(final_conc, start_conc, final_vol):
    #     transfer_vol.append(vol*round(final/start, 1))
    # for s_vol, f_vol in zip(transfer_vol, final_vol):
    #     nfw_vol.append(f_vol-s_vol)
    # lists = [well_list, sample_mass, sample_vol, final_mass, final_vol,
    #          start_conc, final_conc, transfer_vol, nfw_vol]
    # # clean up bad wells from lists
    # for i, (start, final) in enumerate(zip(start_conc, final_conc)):
    #     if start < final:
    #         bad_wells.append(well_list[i])
    #         for list in lists:
    #             del list[i]

    # Reagents and Well Lists

    nfw_source = reagent_tubes.wells()[0]

    tips20 = [ctx.load_labware('opentrons_96_filtertiprack_20ul', slot)
              for slot in ['3', '6'][:math.ceil(len(well_list)/48)]]
    tips300 = [ctx.load_labware('opentrons_96_filtertiprack_200ul', slot)
               for slot in ['5', '7'][:math.ceil(len(well_list)/48)]]
    p20 = ctx.load_instrument('p20_single_gen2', p20_mount, tip_racks=tips20)
    p300 = ctx.load_instrument('p300_single_gen2', p300_mount,
                               tip_racks=tips300)

    # tips20 = [ctx.load_labware('opentrons_96_filtertiprack_20ul', 3)]
    # tips300 = [ctx.load_labware('opentrons_96_filtertiprack_200ul', 5)]
    # p20 = ctx.load_instrument('p20_single_gen2', p20_mount, tip_racks=tips20)
    # p300 = ctx.load_instrument('p300_single_gen2', p300_mount,
    #                            tip_racks=tips300)

    # liquid height tracking
    v_naught_dil = vol_water*1000
    radius = reagent_tubes.wells()[0].diameter/2
    h_naught_water = 0.85*v_naught_dil/(math.pi*radius**2)
    h = h_naught_water

    def adjust_height(vol):
        nonlocal h
        dh = vol/(math.pi*radius**2)
        h -= dh
        if h < 12:
            h = 1

    # do NFW addition first to save tips, mix after sample addition
    ctx.comment('\n\n~~~~~~~~~~~~~~ADDING NFW TO WELLS~~~~~~~~~~~~~~~\n')
    p20.pick_up_tip()
    p300.pick_up_tip()
    for nfw, d in zip(nfw_vol, well_list):
        if nfw >= 20:
            pip = p300
        else:
            pip = p20
        pip.transfer(nfw, nfw_source.bottom(h), dest_plate[d],
                     new_tip='never')
        adjust_height(nfw)
    p20.drop_tip()
    p300.drop_tip()

    ctx.comment('\n\n~~~~~~~~~~~~~TRANSFERRING SAMPLE VOLUMES~~~~~~~~~~~~~~\n')
    for t_vol, well, f_vol in zip(transfer_vol, well_list, final_vol):
        if t_vol >= 20:
            pip = p300
        elif t_vol <= 0:
            continue
        else:
            pip = p20

        pip.pick_up_tip()
        pip.transfer(t_vol, source_plate.wells_by_name()[well],
                     dest_plate.wells_by_name()[well], new_tip='never')
        # there is an error here when the water volume is high but hte sample volume is low, sample pipette can end up too small to mix half the sample
        pip.mix(1, f_vol/2, dest_plate.wells_by_name()[well])
        pip.drop_tip()

    # bad_list = [well.display_name.split(' ')[0] for well in bad_wells]
    # print(lists)

    if len(bad_wells) > 0:
        bad_msg = '\n\n'.join(bad_wells)
        ctx.comment(f'The following sample wells failed: \n\n{bad_msg}')

    for c in ctx.commands():
        print(c)
