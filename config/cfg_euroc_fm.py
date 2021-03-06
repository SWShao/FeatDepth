DEPTH_LAYERS = 50
POSE_LAYERS = 18
FRAME_IDS = [0, -1, 1, 's']
IMGS_PER_GPU = 2
HEIGHT = 480
WIDTH = 768

data = dict(
    name = 'euroc',
    split = 'exp',
    height = HEIGHT,
    width = WIDTH,
    frame_ids = FRAME_IDS,
    in_path = '/ssd/EuRoc/MH_02_easy',#'/ssd/EuRoc/MH_02_easy','/ssd/EuRoc/MH_04_difficult'
    gt_depth_path = None,
    png = True,
    stereo_scale = True if 's' in FRAME_IDS else False,
)

model = dict(
    name = 'mono_fm',
    depth_num_layers = DEPTH_LAYERS,
    pose_num_layers = POSE_LAYERS,
    frame_ids = FRAME_IDS,
    imgs_per_gpu = IMGS_PER_GPU,
    height = HEIGHT,
    width = WIDTH,
    scales = [0, 1, 2, 3],
    min_depth = 0.1,
    max_depth = 50.0,
    depth_pretrained_path = '/node01/jobs/io/pretrained/checkpoints/resnet/resnet{}.pth'.format(DEPTH_LAYERS),
    pose_pretrained_path =  '/node01/jobs/io/pretrained/checkpoints/resnet/resnet{}.pth'.format(POSE_LAYERS),
    extractor_pretrained_path = '/node01/jobs/io/out/changshu/autoencoder_euroc/epoch_30.pth',
    automask = False,
    disp_norm = False,
    perception_weight = 1e-3,
    smoothness_weight = 1e-3,
)

# resume_from = '/node01/jobs/io/out/changshu/fm_euroc/epoch_40.pth'
resume_from = None
finetune = None
total_epochs = 80
imgs_per_gpu = IMGS_PER_GPU
learning_rate = 1e-4
workers_per_gpu = 4
validate = False

optimizer = dict(type='Adam', lr=learning_rate, weight_decay=0)
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=1.0 / 3,
    step=[20,30],
    gamma=0.5,
)

checkpoint_config = dict(interval=1)
log_config = dict(interval=5,
                  hooks=[dict(type='TextLoggerHook'),])
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
workflow = [('train', 1)]