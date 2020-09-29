import argparse
import logging
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


def list_to_str(*items: str, is_wrap_in_ticks: bool = False) -> str:
    if is_wrap_in_ticks:
        items = list(items)
        for idx in range(len(items)):
            items[idx] = f'`{items[idx]}`'
    if len(items) == 0:
        raise ValueError("Must have at least one item")
    elif len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return f'{items[0]} and {items[1]}'
    else:
        return ', '.join(items[:-1]) + f', and {items[-1]}'


def make_warning_pr(
        base_branch: str,
        package_name: str,
        assignee: str,
        *warnings: str,
        is_no_change: bool = False,
        is_dry_run: bool = False,
):
    title = f'[{package_name}] Add warnings'
    body = f'This PR enables {list_to_str(*warnings, is_wrap_in_ticks=True)} in `{package_name}`.'
    if is_no_change:
        body += " No source code was modified to enable these warnings."
    return make_pr(
        title=title,
        body=body,
        base_branch=base_branch,
        assignee=assignee,
        is_dry_run=is_dry_run,
    )


def make_pr(
        title: str,
        body: str,
        base_branch: str,
        assignee: str,
        is_dry_run: bool = False,
):
    command = [
        'gh', 'pr', 'create',
        '--title', title,
        '--body', body,
        '--base', base_branch,
        '--assignee', assignee,
    ]
    if is_dry_run:
        print(f"Command would be '{' '.join(command)}'")
    else:
        logger.info("Creating PR")
        return subprocess.run(command)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('package', type=str, help='The package name')
    parser.add_argument('base_branch', type=str, help='The branch name to merge into')
    parser.add_argument('warnings', type=str, help='The warnings to mention in the PR')
    parser.add_argument('--is-no-change',
                        default=False, action='store_true',
                        help='Has the source code been changed?')
    parser.add_argument('-a', '--assignee', type=str,
                        help='Who should be assigned to the PR')
    parser.add_argument('-d', '--dry-run', '-d',
                        default=False, action='store_true',
                        help="Output the command that would be used")
    args = parser.parse_args()
    warnings = args.warnings.strip().split()
    make_warning_pr(
        args.base_branch,
        args.package,
        args.assignee,
        *warnings,
        is_no_change=args.is_no_change,
        is_dry_run=args.dry_run,
    )


if __name__ == '__main__':
    main()
