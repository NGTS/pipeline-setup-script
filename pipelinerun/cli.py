from .render import RendersTemplate


def create_run_script(args):
    r = RendersTemplate()
    text = r.render(
        date=args.date,
        bias=args.bias,
        dark=args.dark,
        flat=args.flat,
        science=args.science,
        pipeline_sha=args.pipeline_sha,
        planetname=args.planetname,
        camera_id=args.camera_id)

    with open(args.output, 'w') as outfile:
        outfile.write(text + '\n')
