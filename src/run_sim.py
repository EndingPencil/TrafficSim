import os
import sys
import traci

# 1. Configuration
SUMO_BINARY = "sumo-gui"  # Opens the visual window
CONFIG_FILE = "../config/simulation.sumocfg"  # Path to your map config

# 2. Check environment
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# 3. Start Simulation
def run():
    # Start the simulation with the config file
    traci.start([SUMO_BINARY, "-c", CONFIG_FILE])
    
    step = 0
    while step < 1000:
        traci.simulationStep()  # Advance one time step
        
        # Simple test: Count vehicles
        vehicle_count = traci.vehicle.getIDCount()
        if step % 100 == 0:
            print(f"Step {step}: {vehicle_count} vehicles active")
            
        step += 1
    
    traci.close()

if __name__ == "__main__":
    run()