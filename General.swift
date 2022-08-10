//© 2022 NaveenKumar MuraliTharan. All Rights Reserved.
import Foundation

public protocol LocalizationParsing: RawRepresentable {
    func localizeString(_ arguments: String...) -> String
}

extension LocalizationParsing where RawValue == String {
    public func localizeString(_ arguments: String...) -> String {
        let argument = arguments.map { $0 as CVarArg }
        let bundle = Localization.customLanguageBundle ?? Bundle.module
        let value = String(format: NSLocalizedString(self.rawValue,bundle: bundle, value: "", comment: "Chats Module"), arguments: argument)
        if self.rawValue == value, let fallback = Localization.fallbackBundle {
            return String(format: NSLocalizedString(self.rawValue,bundle: fallback, value: "", comment: "Chats Module"), arguments: argument)
        }
        return value
    }
}

public struct Localization {
    static var fallbackBundle: Bundle? = {
        let fallbackLanguage = "en"
        guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return nil }
        guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return nil }
        return fallbackBundle
    }()
    
    static var customLanguageBundle: Bundle?
    public static var customLocale: Locale?
    
    public static var customLanguage: String? {
        didSet {
            if oldValue != customLanguage {
                guard let language = customLanguage else {
                    customLanguageBundle = nil
                    customLocale = nil
                    return
                }
                guard let bundlePath = Bundle.module.path(forResource: language, ofType: "lproj") else {
                    customLanguageBundle = nil
                    customLocale = nil
                    return
                }
                guard let bundle = Bundle(path: bundlePath) else {
                    customLanguageBundle = nil
                    customLocale = nil
                    return
                }
                customLanguageBundle = bundle
                customLocale = Locale.init(identifier: language)
            }
            
        }
    }
    
    
    // <--- Module Wise Dividing --->
    public enum CommonContents: String, LocalizationParsing, CaseIterable {
        case search = "chat.search.widget.hint"
        case cancel = "vcancel"
        case noresultsfound = "consents.form.select.search.empty"
        case copy = "chat.action.bottomsheet.copy"
        case apply = "chat.settings.theme.applytext"
        case set = "settings_chatbg_group_dialog_positive"
        case save = "chat.chatactions.title.save"
        case leave = "chat_actions_chat_leave"
        case you = "chat.sender.you"
        case remove = "chat.profile.upload.option.remove"
        case more = "chat.custommessage.dialog.title"
        case next = "settings.action.privacy.lock.next"
        case send = "gallery.send"
        case connectInternet = "cliq.operation.network.fail"
        case okOperation = "chat.share.contact.failure.ok"// "cliq.operation.ok"
        case failOperation = "info_call_failed"//"cliq.operation.failed"
        case back = "chat_message_card_navigate_back"//"cliq.back"
        case delete = "chat.history.delete"
        case information = "chat_details_info"
        case tryAgainLater = "cliq.operation.tryagain"
        case networkFail = "cliq.operation.networkfail"
        case add = "chat_message_mention_add"
        case zohoLinkPreview = "unfurl_consent_title"
        case contentLink = "unfurl_consent_desc"
        case setInSettings = "cliq.link.preview.prompt.note"
        case rememberMyChoice = "cliq.link.preview.prompt.remember"
        case restrict = "unfurl_consent_restrict"
        case allow = "chat.dialog.permission.allow"
        case original = "arattai.media.crop.original"
        case later = "chat.dialog.negativebutton.later"
        case doubleQuotes = "cliq.signUp.header"
        case open = "cliq.link.open"
        case accept = "chat.contact.invite.accept"
        case noThanks = "cliq.operation.nothanks"
        case editTitle = "chat.actions.edit.text"
        case defaultTitle = "cliq.settings.notification.systemSound"
        case linkCopySuccess = "cliq.link.copied.success"
        case copyMessageLink = "cliq.copy.message.link"
        case doneTitle = "chat_title_edit_done"
        case filter = "COM.DOCSCANNER.SDK.FILTER"
        case notNow = "chat.dialog.permission.negativetext"
        case conform = "popup_with_input_title"
        case someThingWrong = "cliq.reminders.feedback.somethingWentWrong"
        case copiedMessage = "chat.actions.copy.success"
        case manageTitle = "arattai.manage"
        case seeMore = "arattai.seeMore"
        case allTitle = "chat.settings.contacts.viewcontacts.all"
        case close = "arattai.CloseText"
        case create = "chat.text.create.channel"
        case typing = "chat.status.typing"
        case personTyping = "cliq.operation.typing.name"
        case noNet = "chat.network.nointernet"
        case mute = "chat_action_bottomsheet_mute"
        case retry = "cliq.message.fail.retry"
        case retryAll = "cliq.message.fail.retry.all"
        case share = "chat.actions.sharecontact.share"
        case processing = "chat_scanner_chat_scanner_processing"
        case skip = "arattai.common.skip.title"
        case noLimit = "arattai.common.nolimit.title"
        case somethingWentWrong = "arattai.common.something.went.wrong.title"
        case joined = "arattai.channel.link.joined.subtitle"
        case noneJoined = "arattai.channel.link.joined.none.subtitle"
        case yetToJoin = "huddle_yet_to_join"
        case deleteAll = "chat_history_delete_all"
        case createdBy = "chat.actions.details.creator.key"
        case inviteLinkCopied = "arattai.common.permalink.copied"
        case alreadyPresentMsg = "arattai.common.already.present.message"
        case noExpiry = "arattai.common.noexpiry.title"
        case hangOnSec = "cliq.loader.hang"// =  "Hang on a sec!";
        case photoSingular = "cliqwatch.title.photo"// = "Photo";//14(Already In Kit)
        
    }
    public enum Onboarding: String, LocalizationParsing, CaseIterable {
        case welcome = "login_ob_title"
        case description = "login_ob_subtitle"
        case linkdescription = "login_ob_subtitle1"
        case startButton = "login_ob_btn"
        case termsofservice = "settings.security.tos"
        case privatepolicy = "settings.security.privacy"
        case initialize = "arattai.loader.title"
        case content = "arattai.loader.subtitle"
        case continueButton = "chat_call_dialog_pbtn"
        case onboardBeta = "chat_onboarding_block_subtext"
        case haiThereContent = "cliq.beta.header"
        case signIn = "chat.login.signin"
        case onBoardError = "cliq.onboaridng.general.error"
        case title = "chat.actions.details.title.key"
        case rateTitle = "cliq.rate.title"
        case rateMessage = "cliq.rate.message"
        case rate = "cliq.rate.rate"
        case rateCancel = "cliq.rate.cancel"
        case rateReLogin = "cliq.video.relogin"
        case newUpdate = "cliq.oauth.scopeEnhance.alert.title"
        case newUpdateMessage = "cliq.oauth.scopeEnhance.alert.message"
        case supportAnyMore = "chat.version.unsupportedtext1"// = "This version of %@ isn’t supported anymore.";
        case upgradeContent = "chat.version.unsupportedtext2"// = "Please upgrade to continue using %@.";
        case upgradeNow = "chat.version.update"// = "Upgrade Now";
        case remaindLater = "cliq.contact.invite.remindmelater"// = "Remind me later";
        case hasJoinedArattai = "chat_user_joined"
        case signInFail = "cliq.operation.signout.fail"
        
        
    }
    public enum FeatureDiscoveredTitle: String, LocalizationParsing, CaseIterable {
        case quickChat = "fd_quickchat_title"
        case effectiveSearch = "cliq.featurediscover.effectiveSearch.title"
        case moreOption = "fd_chat_long_press_title"
        case chatInfo = "fd_header_actions_title"
        case starMessage = "cliq.featurediscover.starMessage.title"
        case videoCall = "fd_call_title"
        case animatedEmoji = "fd_zomoji_title"
        case channelsCreation = "fd_new_channel_title"
        case contactInvite = "fd_invite_title"
        case muteChannel = "cliq.featurediscover.muteChannel.title"
        case unReadMessage = "fd_unread_title"
        case setStatus = "chat.settings.status.customstatus"
        case forkMessage = "fd_fork_title"
        case audioRecording = "fd_record_title"
        case mentions = "fd_mention_title"
        case attachment = "fd_share_title"
        case longTapMessage = "fd_msg_long_press_title"
        case siriShortcutPrompt
        case reactions = "fd_reaction_title"
        case swipeToReply
        case swipeToReplyNew = "cliq.featurediscover.swipeToReplyNew.title"
        
        case reminderDialoguePrompt
        case reminderMessageAction
        case stickers
    }
    public enum FeatureDiscoveredSubTitle: String, LocalizationParsing, CaseIterable {
        case quickChat = "fd_quickchat_desc"
        case effectiveSearch = "cliq.featurediscover.effectiveSearch.subtitle"
        case moreOption = "fd_chat_long_press_desc"
        case chatInfo = "cliq.featurediscover.chatInfo.subtitle"
        case starMessage = "cliq.featurediscover.starMessage.subtitle"
        case videoCall = "fd_call_desc"
        case animatedEmoji = "fd_zomoji_desc"
        case channelsCreation = "fd_new_channel_desc"
        case contactInvite = "fd_invite_desc"
        case muteChannel = "cliq.featurediscover.muteChannel.subtitle"
        case unReadMessage = "fd_unread_desc"
        case setStatus = "fd_status_desc"
        case forkMessage = "fd_fork_desc"
        case audioRecording = "fd_record_desc"
        case mentions = "fd_mention_desc"
        case attachment = "fd_share_desc"
        case longTapMessage = "fd_msg_long_press_desc"
        case siriShortcutPrompt
        case reactions = "fd_reaction_desc"
        case swipeToReply
        case swipeToReplyNew = "cliq.featurediscover.swipeToReplyNew.subtitle"
        
        case reminderDialoguePrompt
        case reminderMessageAction
        case stickers
        
    }
    public enum Watch: String, LocalizationParsing, CaseIterable {
        case loginApplication = "cliqwatch.notLoginState.text"// = "Please login to %@ app before opening in your watch";//4
        case startConversation = "cliqwatch.emptyChatWindow.text"// = "This place will not look deserted once you start conversing.";//5
        case quiteEmpty = "cliqwatch.emptyMessageWindow.text"// = "This place looks quite empty.";//8
        case networkCheck = "cliqwatch.connectionlost.text"// = "Looks like a lapse in connection. Please check your network.";//7

        case currentLocation = "cliqwatch.currentLocationButton.title"// = "Current Location";//15
        case viewOnPhone = "cliqwatch.viewonphoneButton.title"// = "View On Phone";//9

        case email = "cliqwatch.info.emailSubTitle.email"// = "Email";//13
        
//        "cliqwatch.title.message" = "Message";//10(Already In Kit)

        case openNotification = "cliqwatch.notification.title"// = "Open this notification on your phone to view the message from your Apple Watch";//1
        case msgFromWatch = "cliqwatch.notificationalert.title" //= "Message from your Apple Watch";//2
        case openMsgHere = "cliqwatch.notificationalert.mesage"// = "Open the message here?";//3
        case couldNotReach = "cliqwatch.noConnection.text" //= "Apple Watch Couldn’t Reach your phone";//6
//        "cliqwatch.userInfo.Offline.text" = "Offline";//11(Already In Kit)
//        "cliqwatch.userInfo.Online.text" = "Online";//12(Already In Kit)
        case turnOnLocationService = "cliqwatch.permissionAccess.text" //= "Please turn on location service from your iPhone";//16

    }
}



//-----------trimmed Code for localization-----------------
/*public enum Language_call: String {
 case bn = "bn-IN"
 case de = "de"
 case el = "el"
 case en = "en"
 case sp = "es"
 case fr = "fr"
 case gu = "gu"
 case hi = "hi"
 case it = "it"
 case ja = "ja"
 case kn = "kn"
 case ml = "ml"
 case mr = "mr"
 case nl = "nl"
 case pa = "pa"
 case pt = "pt-PT"
 case ru = "ru"
 case ta = "ta-IN"
 case te = "te"
 case tr = "tr"
 case ur = "ur-Arab-IN"
 case vi = "vi"
 case zhHans = "zh-Hans"
 case zhHant = "zh-Hant"
 public func changeToSelected() -> String {
 return self.rawValue
 }
 }
 
 public func language_Output(string: String, value: String, arguments: [CVarArg]) -> String {
 let fallbackLanguage = "en"
 guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 guard
 let bundlePath = Bundle.module.path(forResource: string, ofType: "lproj"),
 let bundle = Bundle(path: bundlePath)
 else { return "" }
 return String(format:  NSLocalizedString(value, bundle: bundle, value: fallbackString, comment: "Language Change"), arguments: arguments)
 }
 public func language_FallBack(value: String, arguments: [CVarArg]) -> String{
 
 if Localization.language == false {
 let regionalLanguage = ["ta", "gu", "ml", "bn", "kn", "mr", "pa", "te", "ur"]
 for language in regionalLanguage {
 if Locale.autoupdatingCurrent.languageCode == language {
 return language_Output(string: Language_call.en.changeToSelected(), value: value, arguments: arguments)
 }
 }
 if Locale.autoupdatingCurrent.languageCode == "pt" {
 return language_Output(string: Language_call.pt.changeToSelected(), value: value, arguments: arguments)
 }
 else if Locale.current.identifier == "zh-Hans_US" {
 return language_Output(string: Language_call.zhHans.changeToSelected(), value: value, arguments: arguments)
 }
 else if Locale.current.identifier == "zh-Hant_US" {
 return language_Output(string: Language_call.zhHant.changeToSelected(), value: value, arguments: arguments)
 }
 var name = ""
 let foreign = ["en", "ru", "hi", "de", "el", "es", "fr", "it", "ja", "nl", "tr", "vi"]
 for foreign in foreign {
 if Locale.autoupdatingCurrent.languageCode == foreign {
 name = language_Output(string: (Language_call.init(rawValue: foreign)?.changeToSelected())!, value: value, arguments: arguments)
 }
 }
 return name
 }
 else {
 if Locale.current.identifier == "zh-Hans_US" {
 return language_Output(string: Language_call.zhHans.changeToSelected(), value: value, arguments: arguments)
 }
 else if Locale.current.identifier == "zh-Hant_US" {
 return language_Output(string: Language_call.zhHant.changeToSelected(), value: value, arguments: arguments)
 }
 let specialCaseLanguagesMain = ["ta", "bn", "pt", "ur"]
 let specialCaseLanguagesSub = ["ta-IN", "bn-IN", "pt-PT", "ur-Arab-IN"]
 
 let languageChnage = Locale.autoupdatingCurrent.languageCode
 guard
 let bundlePath = Bundle.module.path(forResource: languageChnage, ofType: "lproj"),
 let bundle = Bundle(path: bundlePath)
 else {
 var name = ""
 for langMain in specialCaseLanguagesMain {
 if Locale.autoupdatingCurrent.languageCode == langMain {
 let index = specialCaseLanguagesMain.firstIndex(of: langMain)
 name = language_Output(string: Language_call.init(rawValue: specialCaseLanguagesSub[index!])!.changeToSelected(), value: value, arguments: arguments)
 }
 }
 return name
 }
 let allLanguage = ["en", "ru", "hi", "de", "el", "es", "fr", "it", "ja", "nl", "tr", "vi", "gu", "ml", "kn", "mr", "pa",  "te"]
 var allLanguageReturn = ""
 for allLanguage in allLanguage {
 if Locale.autoupdatingCurrent.languageCode == allLanguage {
 allLanguageReturn = language_Output(string: Language_call.init(rawValue: allLanguage)!.changeToSelected(), value: value, arguments: arguments)
 }
 }
 
 return allLanguageReturn
 }
 }
 
 
 
 
 //-------reference------------
 //public enum OrderStatus {
 //    case pending, processing, complete, canceled, no_Of_Project_Completed(String), chat_add_group_error(String), chat_add_error(String, String)
 //    public var displayName:  String {
 //        switch self {
 //        case .complete:
 //            return NSLocalizedString("Project_Status_Completed",bundle: .module ,comment: "Completed")// Normal translation
 //        case .pending:
 //            return NSLocalizedString("Project_Status_Pending",bundle: .module, comment: "Pending")
 //        case .processing:
 //            return NSLocalizedString("Project_Status_Processing",bundle: .module, comment: "Processing")
 //        case .canceled:
 //            return NSLocalizedString("Project_Status_Cancelled",bundle: .module, comment: "Cancelled")
 //        case .no_Of_Project_Completed(let progress):
 //            return String(format:  NSLocalizedString("No_Of_Project_Completed",bundle: .module, comment: "Total"), progress)// Translation with one single argument
 //        case .chat_add_group_error(let name):
 //            return String(format:  NSLocalizedString("chat_add_group_error",bundle: .module, comment: "Total"), name, name)// translation with two same arguments
 //
 //        case .chat_add_error(let name, let group):
 //            return String(format: NSLocalizedString("chat_add_error",bundle: .module, comment: "Total"), name, group)// translation with two different arguments
 //        }
 //    }
 //}
 
 
 //    public enum Plurals {
 //        case addUsers(Bool, String), deleteUser(String)
 //
 //        public var plurals: String {
 //            switch self {
 //            case .addUsers(let isSingle, let contacts):
 ////                if isSingle == true {
 ////                    return NSLocalizedString("arattai.group.add.participants.add", bundle: .module, comment: "One User Added")
 ////                }
 ////                return String (format: NSLocalizedString("arattai.group.add.participants.plural.add", bundle: .module, comment: "More Than One User Added"), contacts)
 //                return (isSingle == true ? NSLocalizedString("arattai.group.add.participants.add", bundle: .module, comment: "One User Added") : String (format: NSLocalizedString("arattai.group.add.participants.plural.add", bundle: .module, comment: "More Than One User Added"), contacts))
 //            case .deleteUser(let contacts):
 //                if contacts == "1" {
 //                    return NSLocalizedString("arattai.group.add.participants.add", bundle: .module, comment: "One User Added")
 //                }
 //                return String (format: NSLocalizedString("arattai.group.add.participants.plural.add", bundle: .module, comment: "More Than One User Added"), contacts)
 //
 //            }
 //        }
 //    }
 
 
 //
 //public func language_FallBack(value: String, arguments: [CVarArg]) -> String{
 //    if Localization.language == false {
 //        let language = ["ta", "gu", "ml", "bn", "kn", "mr", "pa", "te", "ur"]
 //        for language in language {
 //            if Locale.autoupdatingCurrent.languageCode == language {
 //
 //                let fallbackLanguage = "en"
 //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //                guard
 //                    let bundlePath = Bundle.module.path(forResource: "en", ofType: "lproj"),
 //                    let bundle = Bundle(path: bundlePath)
 //                else { return "" }
 //                return String(format:  NSLocalizedString(value, bundle: bundle, value: fallbackString, comment: "Language Change"), arguments: arguments)
 //            }
 //        }
 //        if Locale.autoupdatingCurrent.languageCode == "pt" {
 //            let fallbackLanguage = "en"
 //            guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //            guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //            let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //            guard
 //                let bundlePath = Bundle.module.path(forResource: "pt-PT", ofType: "lproj"),
 //                let bundle = Bundle(path: bundlePath)
 //            else { return "" }
 //            return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //        }
 //        else if Locale.autoupdatingCurrent.languageCode == "zh" {
 //            let fallbackLanguage = "en"
 //            guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //            guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //            let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //            guard
 //                let bundlePath = Bundle.module.path(forResource: "zh-Hans", ofType: "lproj"),
 //                let bundle = Bundle(path: bundlePath)
 //            else { return "" }
 //            return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //        }
 //        var name = ""
 //        let foreign = ["en", "ru", "hi", "de", "el", "es", "fr", "it", "ja", "nl", "tr", "vi"]
 //        for foreign in foreign {
 //            if Locale.autoupdatingCurrent.languageCode == foreign {
 //                let fallbackLanguage = "en"
 //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //                guard
 //                    let bundlePath = Bundle.module.path(forResource: foreign, ofType: "lproj"),
 //                    let bundle = Bundle(path: bundlePath)
 //                else { return "" }
 //                name = String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //            }
 //        }
 //        return name
 //    }
 //    else {
 //        let specialCaseLanguagesMain = ["ta", "bn", "pt", "ur", "zh"]
 //        let specialCaseLanguagesSub = ["ta-IN", "bn-IN", "pt-PT", "ur-Arab-IN", "zh-Hans"]
 //
 //        let languageChnage = Locale.autoupdatingCurrent.languageCode
 //        guard
 //            let bundlePath = Bundle.module.path(forResource: languageChnage, ofType: "lproj"),
 //            let bundle = Bundle(path: bundlePath)
 //        else {
 //            var name = ""
 //            for langMain in specialCaseLanguagesMain {
 //                //print(langMain)
 //                if Locale.autoupdatingCurrent.languageCode == langMain {
 //                    //print(langMain)
 //                    let index = specialCaseLanguagesMain.firstIndex(of: langMain) // 0
 //                    //print(index)
 //                    //for langSub in specialCaseLanguagesSub{
 //                    //                    print(langSub.count)
 //                    guard
 //                        let bundlePath = Bundle.module.path(forResource: specialCaseLanguagesSub[index!], ofType: "lproj"),
 //                        let bundle = Bundle(path: bundlePath)
 //                    else { return "" }
 //                    let fallbackLanguage = "en"
 //                    guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //                    guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //                    let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //                    name = String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //                    //            }
 //                }
 //            }
 //            return name
 //        }
 //
 //        //            else if Locale.autoupdatingCurrent.languageCode == "bn"{
 //        //                guard
 //        //                    let bundlePath = Bundle.module.path(forResource: "bn-IN", ofType: "lproj"),
 //        //                    let bundle = Bundle(path: bundlePath)
 //        //                else { return "" }
 //        //                let fallbackLanguage = "en"
 //        //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //        //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //        //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //        //                return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //        //            }
 //        //            else if Locale.autoupdatingCurrent.languageCode == "pt"{
 //        //                guard
 //        //                    let bundlePath = Bundle.module.path(forResource: "pt-PT", ofType: "lproj"),
 //        //                    let bundle = Bundle(path: bundlePath)
 //        //                else { return "" }
 //        //                let fallbackLanguage = "en"
 //        //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //        //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //        //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //        //                return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //        //            }
 //        //            else if Locale.autoupdatingCurrent.languageCode == "ur"{
 //        //                guard
 //        //                    let bundlePath = Bundle.module.path(forResource: "ur-Arab-IN", ofType: "lproj"),
 //        //                    let bundle = Bundle(path: bundlePath)
 //        //                else { return "" }
 //        //                let fallbackLanguage = "en"
 //        //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //        //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //        //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //        //                return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //        //            }
 //        //            else if Locale.autoupdatingCurrent.languageCode == "zh"{
 //        //                guard
 //        //                    let bundlePath = Bundle.module.path(forResource: "zh-Hans", ofType: "lproj"),
 //                    let bundle = Bundle(path: bundlePath)
 //                else { return "" }
 //                let fallbackLanguage = "en"
 //                guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //                guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //                let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //                return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //            }
 //            else { return "" }
 //        }
 //        let fallbackLanguage = "en"
 //        guard let fallbackBundlePath = Bundle.module.path(forResource: fallbackLanguage, ofType: "lproj") else { return value }
 //        guard let fallbackBundle = Bundle(path: fallbackBundlePath) else { return value}
 //        let fallbackString = fallbackBundle.localizedString(forKey: value, value: "", table: "")
 //        return String(format: NSLocalizedString(value,bundle: bundle, value: fallbackString, comment: "Chats Module"), arguments: arguments)
 //    }
 //}
 */
