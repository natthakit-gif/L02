def ch4combus(methane_g, oxygen_g):
    # Molar masses (g/mol)
    CH4_MW = 12.011 + 4 * 1.008
    O2_MW = 2 * 15.999
    CO2_MW = 12.011 + 2 * 15.999
    H2O_MW = 2 * 1.008 + 15.999

    # Number of moles
    n_CH4 = methane_g / CH4_MW
    n_O2 = oxygen_g / O2_MW

    # Stoichiometric ratio
    if n_O2 >= 2 * n_CH4:
        n_CO2 = n_CH4
        n_H2O = 2 * n_CH4
        excess_O2 = n_O2 - 2 * n_CH4
        excess_CH4 = 0
    else:
        n_CO2 = n_O2 / 2
        n_H2O = n_O2
        excess_CH4 = n_CH4 - n_O2 / 2
        excess_O2 = 0

    CO2_g = n_CO2 * CO2_MW
    H2O_g = n_H2O * H2O_MW
    excess_CH4_g = excess_CH4 * CH4_MW
    excess_O2_g = excess_O2 * O2_MW

    return excess_CH4_g, excess_O2_g, CO2_g, H2O_g

if __name__ == '__main__':
    m = float(input('Methane (CH4, in g):'))
    o = float(input('Oxygen (O2, in g):'))
    result = ch4combus(m, o)
    print('CH4: %.2f g. O2 %.2f g. CO2 %.2f g. H2O %.2f g' % result)