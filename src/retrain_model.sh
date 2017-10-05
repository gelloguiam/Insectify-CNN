python src/transfer_learning.py \
  --bottleneck_dir="bottlenecks" \
  --how_many_training_steps="500" \
  --model_dir="inception" \
  --summaries_dir="training_summaries/basic" \
  --output_graph="retrained_graph.pb" \
  --output_labels="labels.txt" \
  --image_dir="training_data" \
  --final_tensor_name="final_result"
