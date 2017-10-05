rm -rf bottlenecks/
rm -rf output_graph/
rm -f *.pb
rm -f *.txt

./src/retrain_model.sh
./src/optimize_model.sh

cp optimized_graph.pb graph.pb
mkdir output_graph
mv retrained_graph.pb output_graph/retrained_graph.pb
mv optimized_graph.pb output_graph/optimized_graph.pb
