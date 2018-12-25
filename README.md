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

### Common

#### mark

```swift
// MARK: - <#Title#>
```

### UI

#### image-view

```swift
private let <#name#>ImageView = UIImageView()
```

#### label

```swift
private let <#name#>Label = UILabel()
```

#### button

```swift
private let <#name#>Button = UIButton(type: .custom)
```

#### container-view

```swift
private let <#name#>ContainerView = UIView()
```

### Rx

#### behavior-relay

```swift
private let <#name#>Relay = BehaviorRelay<<#Type#>>(value: <#initialValue#>)
```

#### publish-relay

```swift
private let <#name#>Relay = PublishRelay<<#Type#>>()
```

#### binder

```swift
var <#name#>Binder: Binder<<#type#>> {
    return Binder(self) { base, value in
        <#code#>
    }
}
```

#### var-driver

```swift
var <#name#>Driver: Driver<<#type#>> {
    return <#code#>
}
```

#### disposebag

```swift
private let disposeBag = DisposeBag()
```

