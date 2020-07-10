data = [{'Particle': 'Strange', 'Class': 'Quark', 'Spin': '1/2', 'Electric charge': '-1/3'},
        {'Particle': 'Charm', 'Class': 'Quark', 'Spin': '1/2', 'Electric charge': '2/3'},
        {'Particle': 'Electron', 'Class': 'Lepton', 'Spin': '1/2', 'Electric charge': '-1'},
        {'Particle': 'Neutrino', 'Class': 'Lepton', 'Spin': '1/2', 'Electric charge': '0'},
        {'Particle': 'Photon', 'Class': 'Boson', 'Spin': '1', 'Electric charge': '0'}]
spin = input()
charge = input()
match_name = [data[x]['Particle'] for x in range(5) if data[x]['Spin'] == spin and data[x]['Electric charge'] == charge]
match_class = [data[x]['Class'] for x in range(5) if data[x]['Spin'] == spin and data[x]['Electric charge'] == charge]

print(match_name[0], match_class[0])
