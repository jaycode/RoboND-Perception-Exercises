import pcl
p = pcl.load("tabletop.pcd", loadRGB=True)

fil = p.make_statistical_outlier_filter()
fil.set_mean_k(50)
fil.set_std_dev_mul_thresh(1.0)

pcl.save(fil.filter(), "tabletop_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "tabletop_outliers.pcd")