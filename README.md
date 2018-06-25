# CodeSnippets
Touch Instinct Xcode snippets.

## How to install

### Install all templates
You can clone the complete project in ```~/Library/Developer/Xcode/UserData/```

OR

Clone/Download the project on your machine and paste the .codesnippets file in ```~/Library/Developer/Xcode/UserData/CodeSnippets/```

### Install partucular templates

#### Install `xcodesnippet`

```sh
./install_xcodesnippet.sh
```

#### Install desired template

```sh
xcodesnippet install Sources/binder.swift
```


## Templates

### mark

```swift
// MARK: - <#Title#>
```

### binder

```swift
var <#name#>Binder: Binder<<#type#>> {
    return Binder(self) { base, value in
        <#code#>
    }
}
```

### configurable-cell

```swift
extension <#CellName#>: ConfigurableCell {

    func configure(with viewModel: <#ViewModelType#>) {
        self.viewModel = viewModel

        <#configuration#>
    }
}
```