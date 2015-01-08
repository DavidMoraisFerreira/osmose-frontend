%rebase('layout.tpl', title=_("Updates summary"))
%def col(t, v):
%            if v > 4.05:
    <{{t}} class="delay-error">\\
%            elif v > 2.05:
    <{{t}} class="delay-warning">\\
%            else:
    <{{t}}>\\
%            end

%end
<table>
%for remote in summary.keys():
<tr><th>{{"0x%03x" % (hash(remote)%4096)}}</th></tr>
<tr><td>
%    for country in summary[remote]:
%        col('span', country['max_age'])
{{country['country']}}<sup>{{country['count']}}</sup>
({{"%0.1f" % country['max_age']}}-{{"%0.1f" % country['min_age']}})
</span>&nbsp;⚫
%    end
</td></tr>
%end
</table>
