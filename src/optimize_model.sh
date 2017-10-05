python -m tensorflow.python.tools.optimize_for_inference \
  --input="output_graph/retrained_graph.pb" \
  --output="output_graph/optimized_graph.pb" \
  --input_names="Mul" \
  --output_names="final_result"
