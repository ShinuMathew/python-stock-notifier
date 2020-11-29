now=$(date +"%T")
echo "====================================================================="
echo "Stock notifier started monitoring product status at : $now...."
echo "====================================================================="
python3 base.py 
echo "=================== NOTIFIER COMPLETED PROCESSING ==================="