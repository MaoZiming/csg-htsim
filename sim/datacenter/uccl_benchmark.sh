./htsim_roce -conns 1024 -nodes 1024 -tm connection_matrices/perm_1024n_1024c_0u_2000000b.cm -strat ecmp_host -paths 8 -log sink -end 2000 -mtu 4000 -switch_latency 0.2 -hop_latency 0.8 -q 200 -seed 13 > roce.out

./htsim_ndp -conns 1024 -nodes 1024 -tm connection_matrices/perm_1024n_1024c_0u_2000000b.cm -strat ecmp_host -paths 8 -log sink -end 2000 -mtu 4000 -switch_latency 0.2 -hop_latency 0.8 -q 200 -seed 13 > ndp.out

./htsim_swift -conns 1024 -nodes 1024 -tm connection_matrices/perm_1024n_1024c_0u_2000000b.cm -end 2000 -mtu 4000 -q 200 -flowsize 2000000 > swift.out

./htsim_swift -conns 1024 -nodes 1024 -tm connection_matrices/perm_1024n_1024c_0u_2000000b.cm -end 2000 -mtu 4000 -q 200 -flowsize 2000000 -subflows 4 > swift_subflow.out

python3 plot_flows.py roce
python3 plot_flows.py ndp
python3 plot_flows.py swift
python3 plot_flows.py swift_subflow