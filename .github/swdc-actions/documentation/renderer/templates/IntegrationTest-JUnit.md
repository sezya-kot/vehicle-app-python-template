# Integration test results

Test results for commit '{{CommitHash}}' run at {{Result.Timestamp}}

Tests     | Failures     | Errors
----------|--------------|--------
{{Result.Tests}} | {{Result.Failures}} | {{Result.Errors}}
{{#Result.TestSuite}}

## Results of test suite `{{name}}`

The following test where executed in test suite `{{name}}`
<table>
<tr><td><b>Name</b></td><td><b>Execution Time</b></td><td><b>Result</b></td></tr>
{{#testcase}}
{{#if failure}}
<tr><td>{{name}}</td><td>{{time}}</td><td>
    failed with error message

    {{{failure}}}
</td></tr>
{{else if error}}
<tr><td>{{name}}</td><td></td><td>
    error during test:

    {{{error.message}}}
</td></tr>
{{else}}
<tr><td>{{name}}</td><td>{{time}}</td><td>passed</td></tr>
{{/if}}
{{/testcase}}
</table>
{{/Result.TestSuite}}

## Original Output

```xml
{{{Result.OriginalOutput}}}
```
