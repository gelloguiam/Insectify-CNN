python src/quantize_graph.py \
  --input="output_graph/optimized_graph.pb" \
  --output="output_graph/quantized_graph.pb" \
  --output_node_names="final_result" \
  --print_nodes \
  --mode=eightbit \
  --logtostderr
