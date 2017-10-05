python src/quantize_graph.py \
  --input="optimized_graph.pb" \
  --output="quantized_graph.pb" \
  --output_node_names="final_result" \
  --print_nodes \
  --mode=eightbit \
  --logtostderr
